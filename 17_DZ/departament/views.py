from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    return render(request, 'departament/index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'departament/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'departament/product_detail.html', {'product': product})



def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'departament/product_detail.html', {'product': product})


