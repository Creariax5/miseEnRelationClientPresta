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
