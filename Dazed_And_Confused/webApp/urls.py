from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from webApp import views

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'registration_page', views.signup, name='registration'),
    url(r'settings_page', views.settings, name='settings'),
    url(r'user_profile', views.user_profile, name='user_profile')
]
