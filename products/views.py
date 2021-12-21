from django.shortcuts import render
from products.models import ProductCategory, Products
# Create your views here.
def products(request):
    category = ProductCategory.objects.all()
    products = Products.objects.all()
    context = {'category':category,'products':products}
    return render(request,'products/index.html', context)

def catproducts(request,slug):
    print('catproduct')
    cat = ProductCategory.objects.filter(slug=slug).first()
    products = Products.objects.filter(category=cat)
    context = {'products':products}
    return render(request,'products/catproducts.html',context)

def productdetail(request,slug):
    print('productdetail')
    product = Products.objects.filter(slug=slug).first()
    context = {'product':product}
    return render(request,'products/productdetail.html',context)
