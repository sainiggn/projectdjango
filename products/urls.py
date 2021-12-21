from django.urls import path
from django.shortcuts import render
from . import views

namespace="products"
urlpatterns = [
    path('',views.products, name='products' ),
    path('<str:slug>',views.catproducts, name='catproducts' ),
    path('<str:slug>/',views.productdetail, name='productdetail' ),
]
