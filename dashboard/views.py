from django.shortcuts import render,HttpResponse,redirect
from home.models import UserProfile,Book
import time
from math import ceil

# Create your views here.

def dashboardHome(request,slug):
    try:
        if request.session['is_seller'] and request.session['seller_slug'] == slug:
            get_seller = UserProfile.objects.get(seller_slug = slug)
            get_all_books = Book.objects.filter(seller = get_seller)
            return render(request,'dashboard.html',{'seller':get_seller,'books':get_all_books})
        else:
            return redirect('/')
    except:
        return redirect('/logout')

def CreateBook(request,slug):
    try:
        if request.session['seller_slug'] == slug:
            get_seller = UserProfile.objects.get(seller_slug = slug)
            if request.method == "POST":
                # calculating sp price
                def discount_calculator(mp,dis):
                    disamount = ceil((int(dis)/100)* int(mp))
                    return int(mp)-disamount
                book_name = request.POST.get('book_name')
                book_description = request.POST.get('book_description')
                book_category = request.POST.get('book_category')
                book_mp_price = request.POST.get('book_price')
                book_discount = request.POST.get('book_discount')
                book_sp_price = discount_calculator(book_mp_price,book_discount)
                book_location = request.POST.get('book_location')
                book_cover = request.FILES['book_cover']
                print(book_cover)
                try:
                    # Get User From Session
                    user = UserProfile.objects.get(seller_slug= slug)
                    save_book = Book(seller=user, book_name= book_name, book_description= book_description,book_category= book_category, book_mp= book_mp_price, book_sp = book_sp_price,book_discount= book_discount, book_cover_photo = book_cover, book_location=book_location)
                    save_book.save()
                    return redirect(f"/dashboard/{slug}")
                except:
                    return HttpResponse('Failed to Save')
            return render(request,'createbook.html',{'seller':get_seller})     
    except:
        return redirect('/')

def RemoveStock(request,slug,bookslug):
    try:
        if request.session['seller_slug'] == slug and request.session['is_seller']:
            find_book = Book.objects.get(book_slug = bookslug)
            find_book.book_status = 'Out of stock'
            find_book.save()
        return redirect(f"/dashboard/{slug}")
    except:
        return redirect('/')
    
def addStock(request,slug,bookslug):
    try:
        if request.session['seller_slug'] == slug and request.session['is_seller']:
            find_book = Book.objects.get(book_slug = bookslug)
            find_book.book_status = 'In Stock'
            find_book.save()
        return redirect(f"/dashboard/{slug}")
    except:
        return redirect('/')
    
    

