from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class SearchForm(ModelForm):
    search = forms.CharField(max_length=50)

    class Meta:
        fields = ('search')
