from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text=None)
    password1 = forms.EmailField(max_length=39, help_text=None)
    password2 = forms.EmailField(max_length=39, help_text=None)


    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', )
