from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
    image = forms.ImageField()


class productForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__' #['name', 'price', ...]
    image = forms.ImageField()

class AddToWishlistForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
