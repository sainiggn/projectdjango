from django.urls import path
from django.shortcuts import render
from . import views

namespace="blog1"
####fk means foreign key
urlpatterns = [
    path('',views.home, name='home' ),
    path('<str:slug>',views.postdetail, name='postdetail' ),
    path('Category/<str:name>',views.postcategory, name='postcategory' ),
]
