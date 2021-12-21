from django.urls import path
from django.shortcuts import render
from . import views

namespace="video"
####fk means foreign key

urlpatterns = [
    path('',views.categorylist, name='catlist' ),
    path('videocomment',views.videocomment, name='videocomment' ),
    path('<slug:slug>',views.videodetail, name='videodetail' ),
    path('<slug:slug>/',views.categoryvideos, name='catvideo' ),
    
    
]
