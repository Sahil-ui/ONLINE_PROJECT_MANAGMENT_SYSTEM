# from django import forms
# from .models import Contact
# 
# class ImageForm(forms.ModelForm):
# 
    # class Meta:
        # model = Contact
        # fields = ['name', 'image']

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']