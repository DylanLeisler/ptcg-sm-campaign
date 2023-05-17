import json
from classes.pokemon import Pokemon, Attack

#TODO: handle missing key exceptions




with open("data/cards/pokemon/sm10.json", "+r") as file:
    clean_cards = []
    card_collection = json.loads(file.read())
    pokemon_cards = [pokemon_card for pokemon_card in filter(lambda x: x["supertype"] == "Pokémon", card_collection)]
    # moveless_pokemon = [pokemon_card for pokemon_card in filter(lambda x: "attacks" not in x.keys(), pokemon_cards)]

    for unclean_card in pokemon_cards:
        for key_tuple in Pokemon.OPTIONAL_KEYS:
            if key_tuple[0] not in unclean_card.keys():
                unclean_card[key_tuple[0]] = key_tuple[1]
        clean_cards.append(unclean_card)


    cards = [Pokemon(card_data["name"],
                card_data["id"], 
                card_data["supertype"],
                card_data["types"][0], 
                card_data["subtypes"],
                # card_data["level"],
                card_data["flavorText"], 
                card_data["abilities"][0], 
                [Attack(attack) for attack in card_data["attacks"]], 
                card_data["evolvesFrom"])
                for card_data in clean_cards]

print(type(cards))
exit()
for card in cards:
    print(card.id)