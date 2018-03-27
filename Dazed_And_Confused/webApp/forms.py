from django.db import models
from django.forms import ModelForm
from django import forms
from .models import User

class UserLogInForm(ModelForm):
    class Meta:
        model = User
        fields=('email', 'password')
    email = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 10)
    
