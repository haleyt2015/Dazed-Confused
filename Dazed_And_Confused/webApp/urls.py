from django.conf.urls import url
from webApp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'registration_page', views.registration, name='registration'),
    url(r'settings_page', views.settings, name='settings'),
]
