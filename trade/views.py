import requests
import json
from django.shortcuts import render, redirect
import sys

sys.path[:0] = ['../']
from authentication.models import Profile
from payment.models import Product
from client.give_pokemon import open_pkb, pkm_str_to_list, pkm_list_to_context, pkm_list_by_nb
from client.give_object import object_str_to_list, object_list_to_context


def trade(request):
    return render(request, "trade.html")


def room(request, nb):
    product = Product.objects.all()
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)

    my_objects = object_str_to_list(profile, current_user)
    product_list = object_list_to_context(product, my_objects)

    value = 2

    if request.method == "POST":
        claim = request.POST['this_id']
        if claim == "1":
            return render(request, "backpack.html", context={"my_objects": my_objects,
                                                             "profile": profile,
                                                             "claim": claim,
                                                             "current_user": current_user})
    return render(request, "room.html", context={"my_objects": my_objects,
                                                 "profile": profile,
                                                 "current_user": current_user,
                                                 "value": value})
