from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import SignUpForm
from .forms import SearchForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
from semantics3 import Products

def home(request):
    return render(request, 'registration/login.html')

def settings(request):
    return render(request, 'settings.html', context=None)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_profile(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, instance=User)
        if form.is_valid():
            search = request.POST.get('search', "")
            sem3 = Products(
                api_key = "SEM3CCB4BBBB383C73986C4B27B9BE4B3088",
                api_secret = "YmJjY2M1YzFlMGM0ZTg1OTdlNDFkYmY5MmRmZTg2ZDk"
            )

            sem3.products_field("search", search)
            results = sem3.get()

        form = SearchForm()
        return render(request, 'user_profile.html', {'form': form , 'results': results})
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         search = form.cleaned_data.get('search')
    #         form.save()
    #         sem3 = Products(
    #             api_key = "SEM3CCB4BBBB383C73986C4B27B9BE4B3088",
    #             api_secret = "YmJjY2M1YzFlMGM0ZTg1OTdlNDFkYmY5MmRmZTg2ZDk"
    #         )
    #
    #         sem3.products_field("search", search)
    #
    #         results = sem3.get()
    #
    #     return render(request, 'user_profile.html', results, {'form': form})

def about_page(request):
    return render(request, 'AboutUs.html')
