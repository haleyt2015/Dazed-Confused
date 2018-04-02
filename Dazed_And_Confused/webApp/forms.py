from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length=254, help_text=None)
    password1 = forms.CharField(max_length=39, help_text=None, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=39, help_text=None, widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
