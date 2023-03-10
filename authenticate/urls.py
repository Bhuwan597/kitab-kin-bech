
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('/register', views.Registration, name='registration'),
    path('/activate', views.Activate, name='activate'),
    path('/login', views.handleLogin, name='handleLogin'),
    path('/password-reset', views.handlePasswordReset, name='handlePasswordReset'),
    path('/password-reset-confirmation', views.passwordRestConfirmation, name='password-rest-confirmation'),
]
