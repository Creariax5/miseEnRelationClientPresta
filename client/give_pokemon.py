import random
from .give_object import give_object


def pkm_str_to_list(profile, current_user):
    my_pokemons = []
    if current_user.is_authenticated:
        for u in profile:
            my_pokemons = u.my_pokemons
        for x in range(len(my_pokemons)):
            my_pokemons = my_pokemons.replace("[", "")
            my_pokemons = my_pokemons.replace("'", "")
            my_pokemons = my_pokemons.replace("]", "")
        my_pokemons = list(my_pokemons.split(", "))
        for i in range(len(my_pokemons)):
            my_pokemons[i] = int(my_pokemons[i])
        if len(my_pokemons) < 722:
            for j in range(722-len(my_pokemons)):
                my_pokemons.append(0)
    print("give_pokemon.pkm_str_to_list")
    return my_pokemons


def pkm_list_to_context(my_list, my_pokemons):
    i = 0
    pokemon_list = []
    for pr in my_list:
        if my_pokemons[i] > 0:
            pokemon_list.append(pr)

        i += 1
    print("give_pokemon.pkm_list_to_context")
    return pokemon_list


def pkm_list_by_nb(pokemons, my_pokemons):
    i = 0
    pokemon_list = []
    for pr in pokemons:
        d = dict()
        if len(my_pokemons) <= i:
            d['nb'] = 0
        else:
            d['nb'] = int(my_pokemons[i])

        d['name'] = pr
        pokemon_list.append(d, )
        i += 1
    print("give_pokemon.pkm_list_by_nb")
    return pokemon_list


def give_pkm(profiles, current_user, nb, pokemon_id, profile):
    for pr in profiles:
        if pr.user.username == current_user.username:
            my_pokemons = pkm_str_to_list(profile, current_user)
            my_object_id = int(my_pokemons[int(pokemon_id) - 1]) + int(nb)
            my_pokemons[int(pokemon_id) - 1] = my_object_id
            pr.my_pokemons = my_pokemons
            pr.save()

            print("add ", nb, " ", pokemon_id)
    print("give_pokemon.give_pkm")


def open_pkb(this_id, profiles, current_user, profile):
    too_many = give_object(profiles, current_user, -1, this_id, profile)
    if too_many:
        if int(this_id) == 1:
            rnd = random.randint(1, 722)
            give_pkm(profiles, current_user, 1, rnd, profile)
        elif int(this_id) == 2:
            rnd = random.randint(1, 722)
            give_pkm(profiles, current_user, 1, rnd, profile)
        elif int(this_id) == 3:
            rnd = random.randint(1, 722)
            give_pkm(profiles, current_user, 1, rnd, profile)
    else:
        print("not enough object")
        return too_many
    print("give_pokemon.open_pkb")
