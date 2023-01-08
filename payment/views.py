from django.shortcuts import render
from .models import Product, Order
from django.http import JsonResponse
import json


def store(request):
    product = Product.objects.all()
    return render(request, "store.html", context={"product": product})


def pay(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "pay.html", context={"product": product})


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    product = Product.objects.get(id=body['productId'])
    Order.objects.create(
        product=product
    )

    return JsonResponse('Payment completed!', safe=False)
