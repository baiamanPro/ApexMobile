from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator
from .models import Product

def home(request):
    products = Product.objects.filter(is_new=True).order_by("-id")[:3]
    return render(request, "main.html", {"products": products})


def catalog_view(request):
    qs = Product.objects.all().order_by("-id")

    paginator = Paginator(qs, 9)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    page_range = paginator.get_elided_page_range(number=page_obj.number)

    return render(request, "products.html", {
        "my_paginator": page_obj,
        "page_range": page_range,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})


