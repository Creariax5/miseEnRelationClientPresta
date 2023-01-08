from django.shortcuts import render
from .models import Product, Order


def store(request):
    product = Product.objects.all()
    return render(request, "store.html", context={"product": product})


def pay(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "pay.html", context={"product": product})
