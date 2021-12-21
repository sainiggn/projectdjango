from django.shortcuts import render
from blog1.models import Category, Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context={'posts':posts}
    return render(request, 'blog1/home.html',context)

def postdetail(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request, 'blog1/postdetail.html',context)

def postcategory(request,name):
    category = Category.objects.filter(name=name).first()
    print(category)
    posts = Post.objects.filter(Category=category)
    context = {'posts':posts}
    return render(request, 'blog1/postcategories.html',context)