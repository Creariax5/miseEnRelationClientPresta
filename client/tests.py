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
        if len(my_objects) <= i:
            d['nb'] = 1
        else:
            d['nb'] = int(my_objects[i])

        d['name'] = pr.name
        print(pr.name)
        d['img'] = pr.img
        product_list.append(d, )

        i += 1
    return product_list


def give_money(profiles, current_user, nb):
    for pr in profiles:
        if pr.user.username == current_user.username:
            pr.money += 100 * int(nb)
            pr.save()
            print("add", current_user.username)


def give_object(profiles, current_user, nb, productId, profile):
    for pr in profiles:
        if pr.user.username == current_user.username:
            my_objects = object_str_to_list(profile, current_user)
            my_object_id = int(my_objects[productId - 1]) + int(nb)
            my_objects[productId - 1] = my_object_id
            pr.my_objects = my_objects
            pr.save()

            print("add ", nb, " ", productId)


def add_pokemon(profile, pokemon_id):
    return "pokemon_list"


def luck_rate(opening_rate, reward_rate):
    return "pokemon_id"


def claim_object(productId, current_user, profiles, product, reward_rate):
    for pr in product:
        if product.category == "pokeball":
            profile = get_current_profile(current_user, profiles)
            for i in range(pr.reward_nb):
                pokemon_id = luck_rate(pr.rate, reward_rate)
                profile.my_pokemon = add_pokemon(current_user, profile, pokemon_id)
                profile.save()
    return "reward"


def get_current_profile(current_user, profiles):
    for pr in profiles:
        if pr.user.username == current_user.username:
            profile = current_user.username
    return profile


'''
def get_current_product(my_filter, product):
    def by_id(productId, product):
        return "pr"

    def by_category(category, product):
        return "pr"
'''
