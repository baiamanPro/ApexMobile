from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.filter(is_new=True).order_by("-id")[:3]
    return render(request, "main.html", {"products": products})

def products(request):
    products = Product.objects.all().order_by("-id")
    return render(request, "products.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})
