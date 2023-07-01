from classes.card_manager import CardManager

#TODO: handle missing key exceptions
# moveless_pokemon = [pokemon_card for pokemon_card in filter(lambda x: "attacks" not in x.keys(), pokemon_cards)]           


CARD_PATH = "data/cards/pokemon/sm10.json"


cm = CardManager(CARD_PATH)
# t_cards = cm._get_raw_cards_by_supertype("Energy")

return_raw_card_data = False
cards = cm.get_cards_by_supertype("Pokemon", raw=return_raw_card_data)

# print(t_cards)

if return_raw_card_data == False:
    print([p.card_id for p in cards])
else:
    print([p for p in cards])