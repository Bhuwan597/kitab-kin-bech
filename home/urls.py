
from django.urls import path,include
from . import views
import dashboard

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login', views.handleLogin, name='login'),
    path('register', views.handleRegister, name='register'),
    path('logout', views.handleLogout, name='logout'),
    path('dashboard', include('dashboard.urls'), name='dashboardhome'),
    path('category/<categoryslug>', views.categoryView, name='categoryview'),
    path('view-book/<bookslug>', views.bookView, name='bookview'),
    path('search', views.handleSearch, name='search'),
    path('store/<storeslug>', views.viewStore, name='store'),

]

