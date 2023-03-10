from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.hashers import make_password,check_password
from home.models import UserProfile
from django.contrib import messages
import secrets
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
# Create your views here.

def Registration(request):
    try:
        if request.session['name'] and request.session['email']:
            return redirect('/')
    except:
        pass
    if request.method == "POST":
        # Getting Form Data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        profile = request.FILES['profile']
        is_seller = request.POST.get('is_seller', False)

        # Form Validation

            # if user already exists
        try:
            user_exists = UserProfile.objects.get(email=email)
            if user_exists:
                return HttpResponse("<h1>User Already Exists</h1>")
        except:
            pass
  
           # Name Validation
        if(name == "" or len(name) > 40):
            return HttpResponse("Invalid Name Input")

            # Email Validation
        if email[-10:] != '@gmail.com':
            return HttpResponse("Invalid Email Input")

            # Phone Validation
        if (str(phone)[:1] != '9' or len(str(phone))!=10 or not str(phone).isnumeric()):
            return HttpResponse("Invalid Phone Input")


            # Address Validation
        if len(address) > 40 :
            return HttpResponse("Invalid Address Input")


            # Password Validation
        if (password != confirm_password or (password == '' or confirm_password =="")):
            return HttpResponse("Invalid Password Input")


            # Photo Validation
        if (profile.size > 2000000):
            return HttpResponse("Invalid Image Size")


        # Password Stuff
        hash_password = make_password(password)


        # Token Generator
        generated_token = secrets.token_hex(24)

        # Creating an Instance to Save
        instance = UserProfile(name = name,email=email,phone=phone,address=address,password=hash_password,profile_photo =profile, is_seller = is_seller, token=generated_token)


        # saving to database
        instance.save()

        # sending email for confirmation
        subject = 'Account Confirmation - KitabKinBech.com'
        from_email = 'bnotes.secure@gmail.com'
        html_content = render_to_string('email_template.html',{'token':generated_token})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject,text_content,from_email,[email])
        msg.attach_alternative(html_content,'text/html')
        msg.send()


        #HTTP Response
        return render(request,'account_verified_template.html',{'name':name,'date_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'title':'Account Registration', 'type':'Registered'})

    else:
        return HttpResponse("Access Denied")
    

def Activate(request):
    try:
        token = request.GET.get('verify_token')
        is_he_user = UserProfile.objects.get(token = token, status= 'inactive')
        if is_he_user:
            try:
                is_he_user.status = 'active'
                is_he_user.token = 0
                is_he_user.account_verified_on=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                is_he_user.save()
                return render(request,'account_verified_template.html',{'name':is_he_user.name,'date_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'title':'Account Verification', 'type':'Verified'})
            except:
                return HttpResponse('Failed to confirm your account. Try again!')
        return HttpResponse('Access Denied!')
    except:
        pass
    return HttpResponse('Access Denied!')
    
def handleLogin(request):
    try:
        if request.session['name'] and request.session['email']:
            return redirect('/')
    except:
        pass
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try: 
            user = UserProfile.objects.get(email = email)
            if user:
                if user.status  != 'active':
                    messages.error(request,'Confirm you account first!')
                    return redirect('/login') 
                flag = check_password(password,user.password)
                if flag:
                    request.session['name'] = user.name
                    request.session['email'] = user.email                    
                    request.session['phone'] = user.phone                    
                    request.session['address'] = user.address
                    if user.is_seller  == "True":                                   
                        request.session['is_seller'] = user.is_seller                    
                        request.session['seller_slug'] = user.seller_slug                    
                    return redirect('/')               
                else:
                    messages.error(request,'Invalid Credentials!')
                    return redirect('/login') 
            else:
                messages.error(request,'Invalid Credentials!')
                return redirect('/login')  
        except:
            messages.error(request,'Invalid Credentials!')
            return redirect('/login')
    else:
        return HttpResponse("Access Denied!")
    
def handlePasswordReset(request):
    try:
        if request.session['name'] and request.session['email']:
            return redirect('/logout')
    except:
        pass
    if request.method == "POST":
        reset_email = request.POST.get('reset_email')
        try:
            regenerated_token = secrets.token_hex(24)
            user_exists = UserProfile.objects.get(email = reset_email)
            user_exists.token = regenerated_token
            user_exists.status = 'inactive'
            user_exists.save()

            # sending email for confirmation
            subject = 'Password Reset - KitabKinBech.com'
            from_email = 'KitabKinBech.com'
            html_content = render_to_string('password_reset_email.html',{'token':regenerated_token})
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject,text_content,from_email,[reset_email])
            msg.attach_alternative(html_content,'text/html')
            msg.send()
            return HttpResponse('<h2>Check your email account to reset password.</h2>')
        except:
            messages.error(request,'User not found!')
            return redirect('/login')
    else:
        return HttpResponse('Access Denied!')
    

def passwordRestConfirmation(request):
    try:
        if request.session['name'] and request.session['email']:
            return redirect('/logout')
    except:
        pass
    if request.method == "POST":
        reset_password = request.POST.get('reset_password')
        get_token = request.POST.get('reset_token')
        try:
            user = UserProfile.objects.get(token = get_token)
            if user:
                hashed_password = make_password(reset_password)
                user.password = hashed_password
                user.token = '0'
                user.status = 'active'
                user.save()
                return redirect('/login')
            else:
                return HttpResponse('<h1>Access Denied!</h1>')
        except:
            return HttpResponse('<h1>Access Denied!</h1>')   
    else:
        try:
            reset_token = request.GET['verify_token']
            user = UserProfile.objects.get(token = reset_token)
            return render(request,'password_reset.html',{'name':user.name,'date_time':datetime.now().strftime("%d/%m/%Y %H:%M:%S"),'title':'Password Reset', 'type':'Reset','token':reset_token})
        except:
            return HttpResponse('<h1>Access Denied!</h1>')
    return HttpResponse('<h1>Access Denied!</h1>')