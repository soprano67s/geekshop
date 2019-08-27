from django.shortcuts import render

# Create your views here.

def main(request):
    menu = [
        {'href': 'main', 'name': 'HOME'},
        {'href': 'products', 'name': 'PRODUCTS'},
        {'href': 'contacts', 'name': 'CONTACT'}
    ]
    context = {
        'title': 'Home',
        'menu': menu,
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
    links_menu = [
        {'href': 'products_all', 'name': 'ALL'},
        {'href': 'products_home', 'name': 'HOME'},
        {'href': 'products_office', 'name': 'OFFICE'},
        {'href': 'products_furniture', 'name': 'FURNITURE'},
        {'href': 'products_modern', 'name': 'MODERN'},
        {'href': 'products_classic', 'name': 'CLASSIC'}
    ]
    context = {
        'title': 'Product-details',
        'links_menu': links_menu,
        'menu': menu,
    }
    return render(request, 'product-details.html', context=context)

def products(request):
    menu = [
        {'href': 'main', 'name': 'HOME'},
        {'href': 'products', 'name': 'PRODUCTS'},
        {'href': 'contacts', 'name': 'CONTACT'}
    ]
    links_menu = [
        {'href': 'products_all', 'name': 'ALL'},
        {'href': 'products_home', 'name': 'HOME'},
        {'href': 'products_office', 'name': 'OFFICE'},
        {'href': 'products_furniture', 'name': 'FURNITURE'},
        {'href': 'products_modern', 'name': 'MODERN'},
        {'href': 'products_classic', 'name': 'CLASSIC'}
    ]
    context = {
        'title': 'Products',
        'menu': menu,
        'links_menu': links_menu,
    }
    return render(request, 'products.html', context=context)
