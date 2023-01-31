from django.shortcuts import render, redirect
from .models import Product, Order
from django.http import JsonResponse
import json
import sys

sys.path[:0] = ['../']
from authentication.models import Profile
from client.give_object import object_str_to_list, give_object


def store(request):
    product = Product.objects.all()
    if request.method == "POST":
        nb = request.POST['nb']
        this_id = request.POST['this_id']
        return redirect('pay/' + this_id + '/' + nb)
    else:
        return render(request, "store.html", context={"product": product})


def pay(request, pk, nb):
    product = Product.objects.get(id=pk)

    coin = int(product.price) * 100 / 2.5
    final = coin * nb

    if request.method == "POST":
        panel = request.POST['this_id']
        if panel == "True":
            panel = False
        else:
            panel = True

    return render(request, "pay.html", context={"product": product,
                                                "nb": nb,
                                                "panel": panel,
                                                "coin": coin,
                                                "final": final,})


def paymentComplete(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    body = json.loads(request.body)

    if int(body['productId']) == 2:
        product = Product.objects.get(id=str(int(body['productId'])))
    else:
        product = Product.objects.get(id=str(int(body['productId']) - 1))
    Order.objects.create(
        product=product,
        buyer=current_user.username
    )

    profiles = Profile.objects.all()
    nb = body['number']
    productId = int(body['productId']) - 1

    give_object(profiles, current_user, nb, productId, profile)

    return JsonResponse('Payment completed!', safe=False)
