from django import forms
from .models import Book
from .models import UserProfile
from django.forms.models import inlineformset_factory

class CreateUserForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.CharField(label='Email')
    phone = forms.CharField(label='Phone')
    address = forms.CharField(label='Address')
    password = forms.CharField(label='Password')
    confirm_password = forms.CharField(label='Confirm Password')
    profile_photo = forms.CharField(label='Profile Picture')
    is_seller = forms.BooleanField(label='Seller')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =(
        )

BookFormSet = inlineformset_factory(
    UserProfile,
    Book,
    BookForm,
    can_delete=False,
    extra=0
    )