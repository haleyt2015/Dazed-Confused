from django.conf.urls import url
from django.contrib.auth import views as auth_views
from webApp import views

urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
    url(r'registration_page', views.signup, name='registration'),
    url(r'settings_page', views.settings, name='settings'),
]
