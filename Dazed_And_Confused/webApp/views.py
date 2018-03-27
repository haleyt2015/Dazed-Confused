from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UserLogInForm

from .models import User

def home(request):
    if request.method == 'POST':
        if form.is_valid():
            email = request.POST.get('email', "")
            password = request.POST.get('password', "")
            form.save()
    form = UserLogInForm()
    return render(request, 'login_page.html', {'form': form})

def registration(request):
    return render(request, 'registration_page.html', context=None)

def settings(request):
    return render(request, 'settings.html', context=None)
