from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
]