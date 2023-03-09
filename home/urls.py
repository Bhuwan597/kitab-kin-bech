
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login', views.handleLogin, name='login'),
    path('register', views.handleRegister, name='register'),

]

