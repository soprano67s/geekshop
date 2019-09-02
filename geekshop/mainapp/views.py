from django.shortcuts import render
from .models import Products, ProductCategory

# Create your views here.

def main(request):
    menu = [
        {'href': 'main', 'name': 'HOME'},
        {'href': 'products', 'name': 'PRODUCTS'},
        {'href': 'contacts', 'name': 'CONTACT'}
    ]
    products = Products.objects.all()
    context = {
        'title': 'Home',
        'menu': menu,
        'products': products,
    }
    return render(request, 'index.html', context=context)

def contacts(request):
    menu = [
        {'href': 'main', 'name': 'HOME'},
        {'href': 'products', 'name': 'PRODUCTS'},
        {'href': 'contacts', 'name': 'CONTACT'}
    ]
    context = {
        'title': 'Contacts',
        'menu': menu,
    }
    return render(request, 'contacts.html', context=context)

def product_details(request):
    menu = [
        {'href': 'main', 'name': 'HOME'},
        {'href': 'products', 'name': 'PRODUCTS'},
        {'href': 'contacts', 'name': 'CONTACT'}
    ]
    links_menu = ProductCategory.objects.all()
    context = {
        'title': 'Product-details',
        'links_menu': links_menu,
        'menu': menu,
    }
    return render(request, 'product-details.html', context=context)

def products(request, pk=None):
    products = ProductCategory.objects.filter(id=pk).all()
    print(products)
    menu = [
        {'href': 'main', 'name': 'HOME'},
        {'href': 'products', 'name': 'PRODUCTS'},
        {'href': 'contacts', 'name': 'CONTACT'}
    ]
    links_menu = ProductCategory.objects.all()
    context = {
        'title': 'Products',
        'menu': menu,
        'links_menu': links_menu,
    }
    return render(request, 'products.html', context=context)
