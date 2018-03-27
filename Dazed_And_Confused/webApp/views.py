from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'login_page.html', context=None)

def registration(request):
    return render(request, 'registration_page.html', context=None)

def settings(request):
    return render(request, 'settings.html', context=None)
