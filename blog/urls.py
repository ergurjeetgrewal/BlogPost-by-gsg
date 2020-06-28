from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('postcomment',views.postcomment,name='postcomment'),
    path('<str:slug>',views.blogPost,name='blogpost'),
]