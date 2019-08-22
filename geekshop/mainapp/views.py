from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def product_details(request):
    return render(request, 'product-details.html')

def products(request):
    return render(request, 'products.html')
