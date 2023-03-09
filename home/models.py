from django.db import models
from datetime import datetime
from autoslug import AutoSlugField
# Create your models here.

class UserProfile(models.Model):
    def fileName(instance,filename):
        return '/'.join(['user_images', str(instance.name),filename])
    name = models.CharField(max_length=40, default=None)
    email = models.CharField(max_length=40, default=None,unique=True)
    phone = models.CharField(max_length=20, default=None)
    address = models.CharField(max_length=40, default='')
    password = models.CharField(max_length=200, default=None)
    profile_photo = models.ImageField(upload_to=fileName, blank=True)
    is_seller = models.CharField(max_length=40, default=False)
    seller_slug = AutoSlugField(populate_from='name', unique = True, null=True, default= None)
    date_of_register = models.CharField(max_length=40, default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    token = models.CharField(max_length=200, default='')
    status = models.CharField(max_length=40, default='inactive')
    account_verified_on = models.CharField(max_length=40, default='Not Verified')


    def __str__(self):
        return self.name

class Book(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=30, default=None)
    book_slug = models.CharField(max_length=100, default=None)
    book_description = models.CharField(max_length=50, default=None)
    book_category = models.CharField(max_length=40, default=None)
    book_mp = models.CharField(max_length=10, default=None)
    book_discount = models.CharField(max_length=10, default=None)
    book_sp = models.CharField(max_length=10, default=None)
    book_location = models.CharField(max_length=40, default=None)
    book_cover_photo = models.CharField(max_length=200, default=None)
    date_of_added = models.CharField(max_length=40, default='')
    book_status = models.CharField(max_length=30, default='In Stock')

    def __str__(self):
        return self.book_name