from django.contrib import admin
from .models import Products, ProductCategory
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Products)
