from django.contrib import admin
from products.models import Products, ProductCategory

# Register your models here.

admin.site.register(Products)
admin.site.register(ProductCategory)
