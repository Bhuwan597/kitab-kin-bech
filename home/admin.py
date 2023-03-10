from django.contrib import admin
from .models import Book
from .models import UserProfile

# Register your models here.
# class BookInlineAdmin(admin.TabularInline):
#     model = Book

# class UserProfileAdmin(admin.ModelAdmin):
#     inlines = [BookInlineAdmin]

# admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Book)
admin.site.register(UserProfile)
