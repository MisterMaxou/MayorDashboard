from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^contact$', views.contact, name="contact"),
    url(r'^', views.coming_soon, name="coming_soon"),
]


