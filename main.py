from classes.card_manager import CardManager

#TODO: handle missing key exceptions
# moveless_pokemon = [pokemon_card for pokemon_card in filter(lambda x: "attacks" not in x.keys(), pokemon_cards)]           


CARD_PATH = "data/cards/pokemon/sm10.json"


cm = CardManager(CARD_PATH)
p_cards = cm._get_raw_cards_by_supertype("Pokemon")

return_raw_card_data = False
cards = cm.get_pokemon_cards(raw=return_raw_card_data)

if return_raw_card_data == False:
    print([p.id for p in cards])
else:
    print([p for p in cards])