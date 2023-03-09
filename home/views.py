from django.shortcuts import render
from .forms import CreateUserForm
from .models import UserProfile, Book
from .forms import BookFormSet
# Create your views here.
def homePage(request):
    return render(request,'homepage.html')

def handleLogin(request):
    return render(request,'login.html',)

def handleRegister(request):
    return render(request,'register.html')