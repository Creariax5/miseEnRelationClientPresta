from django.shortcuts import render, redirect
from .models import Product, Order
from django.http import JsonResponse
import json
import sys

sys.path[:0] = ['../']
from authentication.models import Profile
from client.tests import object_str_to_list


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
    return render(request, "pay.html", context={"product": product,
                                                "nb": nb})


def paymentComplete(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    body = json.loads(request.body)
    print('BODY:', body)
    product = Product.objects.get(id=body['productId'])
    Order.objects.create(
        product=product,
        buyer=current_user.username
    )
    profiles = Profile.objects.all()
    nb = body['number']
    productId = int(body['productId'])

    for pr in profiles:
        if pr.user.username == current_user.username:
            my_objects = object_str_to_list(profile, current_user)
            my_object_id = int(my_objects[productId-1])
            my_object_id = int(my_object_id) + 1 * int(nb)
            my_objects[productId-1] = my_object_id
            pr.my_objects = my_objects
            pr.save()

            print("add ", nb, " ", productId)

    if productId == 4:
        for pr in profiles:
            if pr.user.username == current_user.username:
                pr.money += 100 * int(nb)
                pr.save()
                print("add", current_user.username)

    return JsonResponse('Payment completed!', safe=False)
