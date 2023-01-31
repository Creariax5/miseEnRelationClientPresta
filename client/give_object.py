import sys

from django.http import JsonResponse

sys.path[:0] = ['../']
from payment.models import Product, Order
from authentication.models import Profile


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
    print("give_object.object_str_to_list")
    return my_objects


def object_list_to_context(product, my_objects):
    i = 0
    product_list = []
    for pr in product:
        d = dict()
        if len(my_objects) <= i:
            d['nb'] = 0
        else:
            d['nb'] = int(my_objects[i])

        d['name'] = pr.name
        d['img'] = pr.img
        d['id'] = pr.id
        product_list.append(d, )

        i += 1
    print("give_object.object_list_to_context")
    return product_list


def give_object(profiles, current_user, nb, productId, profile):
    too_many = False
    for pr in profiles:
        if pr.user.username == current_user.username:
            if int(nb) < 0:
                my_objects = object_str_to_list(profile, current_user)
                if int(my_objects[int(productId) - 1]) >= 1:
                    too_many = True
                    my_object_id = int(my_objects[int(productId) - 1]) + int(nb)
                    my_objects[int(productId) - 1] = my_object_id
                    pr.my_objects = my_objects
                    pr.save()
            else:
                my_objects = object_str_to_list(profile, current_user)
                my_object_id = int(my_objects[int(productId) - 1]) + int(nb)
                my_objects[int(productId) - 1] = my_object_id
                pr.my_objects = my_objects
                pr.save()

            print("add ", nb, " ", productId)
    print("give_object.give_object")
    return too_many


def give_money(profiles, current_user, nb):
    for pr in profiles:
        if pr.user.username == current_user.username:
            pr.money += 100 * int(nb)
            pr.save()
            print("add", current_user.username)
    print("give_object.give_money")


def coin_pay(final, profiles, current_user):
    for pr in profiles:
        if pr.user.username == current_user.username:
            pr.money -= int(final)
            pr.save()
            print("add", current_user.username)
    print("give_object.give_money")


def coin_payment_complete(request, productId, nb):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)

    if productId == 2:
        product = Product.objects.get(id=str(productId))
    else:
        product = Product.objects.get(id=str(productId - 1))
    Order.objects.create(
        product=product,
        buyer=current_user.username
    )

    profiles = Profile.objects.all()
    productId = productId - 1

    give_object(profiles, current_user, nb, productId, profile)

    return JsonResponse('Payment completed!', safe=False)
