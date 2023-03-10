
from django.urls import path,include
from . import views
app_name = 'dashboard'


urlpatterns = [
    path('/<slug>', views.dashboardHome, name='slug'),
    path('/<slug>/create', views.CreateBook, name='addbook'),
    path('/<slug>/remove-stock/<bookslug>', views.RemoveStock, name='removestock'),
    path('/<slug>/in-stock/<bookslug>', views.addStock, name='addstock'),

]

