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
        print(my_pokemons)
    return my_pokemons


def pkm_list_to_context(my_list, my_pokemons):
    i = 0
    print(my_list)
    pokemon_list = []
    for pr in my_list:
        if my_pokemons[i] > 0:
            pokemon_list.append(pr)

        i += 1

    return pokemon_list


def give_pkm(profiles, current_user, nb, productId, profile):
    for pr in profiles:
        if pr.user.username == current_user.username:
            my_pokemons = pkm_str_to_list(profile, current_user)
            print(nb, my_pokemons, productId)
            my_object_id = int(my_pokemons[int(productId) - 1]) + int(nb)
            my_pokemons[int(productId) - 1] = my_object_id
            print(my_pokemons)
            pr.my_pokemons = my_pokemons
            pr.save()

            print("add ", nb, " ", productId)