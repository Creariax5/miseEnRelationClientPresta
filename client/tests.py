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
