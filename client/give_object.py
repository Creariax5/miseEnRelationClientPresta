import random

from django.test import TestCase


def object_str_to_list(profile, current_user):
    my_objects = []
    if current_user.is_authenticated:
        for u in profile:
            my_objects = u.my_objects
        for x in range(len(my_objects)):
            my_objects = my_objects.replace("[", "")
            my_objects = my_objects.replace("'", "")
            my_objects = my_objects.replace("]", "")
        my_objects = list(my_objects.split(", "))
    return my_objects


def object_list_to_context(product, my_objects):
    i = 0
    product_list = []
    for pr in product:
        d = dict()
        if len(my_objects) <= 0:
            d['nb'] = 1
        else:
            d['nb'] = int(my_objects[i])

        d['name'] = pr.name
        print(pr.name)
        d['img'] = pr.img
        product_list.append(d, )

        i += 1
    return product_list


def give_object(profiles, current_user, nb, productId, profile):
    for pr in profiles:
        if pr.user.username == current_user.username:
            my_objects = object_str_to_list(profile, current_user)
            my_object_id = int(my_objects[productId - 1]) + int(nb)
            my_objects[productId - 1] = my_object_id
            pr.my_objects = my_objects
            pr.save()

            print("add ", nb, " ", productId)


def give_money(profiles, current_user, nb):
    for pr in profiles:
        if pr.user.username == current_user.username:
            pr.money += 100 * int(nb)
            pr.save()
            print("add", current_user.username)
