from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from .models import UserProfile, Book

# Create your views here.
def homePage(request):
    books = Book.objects.filter(book_status = 'In Stock')
    recently_uploaded = Book.objects.filter(book_status='In Stock').order_by('-id')[:5]
    context = []
    categories = ("Text Books","Reference Books","Guide and Guess Papers","Handwritten Notes","Courses","Religious Books", "Motivational Books","Other Books")

    for category in categories:
        temp_list = {
            "category": category,
            "no": Book.objects.filter(book_category = category,book_status='In Stock').count()
        }
        context.append(temp_list)    



    stores = UserProfile.objects.filter( is_seller = 'True')
    return render(request,'homepage.html',{'stores':stores, 'books':books,'categories':context,'recents':recently_uploaded,'populars':recently_uploaded})

def handleLogin(request):
    try:
        if request.session['name'] and request.session['email']:
            return redirect('/')
    except:
        pass
    return render(request,'login.html',)

def handleRegister(request):
    try:
        if request.session['name'] and request.session['email']:
            return redirect('/')
    except:
        pass
    return render(request,'register.html')


def handleLogout(request):
    logout(request)
    if request.session.get('name'):
        try:
            del request.session['name'] 
            del request.session['email']
            del request.session['phone']
            del request.session['address']
            del request.session['is_seller']
            del request.session['seller_slug']
            return redirect('/')
        except:
            return redirect('/')
    return redirect('/')
            
def categoryView(request, categoryslug):
    try:
        context = []
        categories = ("Text Books","Reference Books","Guide and Guess Papers","Handwritten Notes","Courses","Religious Books", "Motivational Books","Other Books")

        for category in categories:
            temp_list = {
                "category": category,
                "no": Book.objects.filter(book_category = category, book_status = 'In Stock').count()
        }
            context.append(temp_list)    

        to_view_books = Book.objects.filter(book_category = categoryslug)
        recently_uploaded = Book.objects.filter(book_status='In Stock').order_by('-id')[:5]
        return render(request, 'category_view.html', {'books': to_view_books,'category':categoryslug,'types':context,'recents':recently_uploaded,'populars':recently_uploaded})
        
    except:
        return redirect('/')
    
def bookView(request, bookslug):
    try:
        if 'name' not in request.session and 'email' not in request.session:
            return redirect('/login')
    except:
        pass

    try:
        recently_uploaded = Book.objects.filter(book_status='In Stock').order_by('-id')[:5]
        context = []
        categories = ("Text Books","Reference Books","Guide and Guess Papers","Handwritten Notes","Courses","Religious Books", "Motivational Books","Other Books")
        for category in categories:
            temp_list = {
            "category": category,
            "no": Book.objects.filter(book_category = category, book_status='In Stock').count()
        }
            context.append(temp_list)    
        book = Book.objects.get(book_slug= bookslug)
        return render(request,'fullpage_book.html',{'book':book,'categories':context,'recents':recently_uploaded,'populars':recently_uploaded})
    except:
        return redirect('/')


def handleSearch(request):
    recently_uploaded = Book.objects.filter(book_status='In Stock').order_by('-id')[:5]
    context = []
    categories = ("Text Books","Reference Books","Guide and Guess Papers","Handwritten Notes","Courses","Religious Books", "Motivational Books","Other Books")
    for category in categories:
        temp_list = {
        "category": category,
        "no": Book.objects.filter(book_category = category, book_status='In Stock').count()
    }
        context.append(temp_list)   
    query = request.GET.get('query')
    if len(query)>50:
            allResults = Book.objects.none()
    else:
        allSearchName = Book.objects.filter(book_name__icontains = query)
        allSearchDescription = Book.objects.filter(book_description__icontains = query)
        allSearchLocation = Book.objects.filter(book_location__icontains = query)
        allResults = allSearchName| allSearchDescription| allSearchLocation
        return render(request,'search.html',{'books':allResults,'categories':context,'recents':recently_uploaded,'populars':recently_uploaded})
    return render(request,'search.html')


def viewStore(request, storeslug):
    recently_uploaded = Book.objects.filter(book_status='In Stock').order_by('-id')[:5]
    context = []
    categories = ("Text Books","Reference Books","Guide and Guess Papers","Handwritten Notes","Courses","Religious Books", "Motivational Books","Other Books")
    for category in categories:
        temp_list = {
        "category": category,
        "no": Book.objects.filter(book_category = category, book_status='In Stock').count()
    }
        context.append(temp_list)   
    try:
        store = UserProfile.objects.get(seller_slug = storeslug)
        books =  Book.objects.filter(seller = store)
        return render(request,'allseller_books.html',{'books':books,'categories':context,'recents':recently_uploaded,'populars':recently_uploaded,'store':store})
    except:
        return redirect('/')