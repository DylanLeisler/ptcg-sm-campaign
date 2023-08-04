from classes.card_manager import CardManager
from classes.deck import Deck
from classes.image_downloader import Image_Downloader
from time import sleep
from django.utils.text import slugify

#TODO: handle missing key exceptions
# moveless_pokemon = [pokemon_card for pokemon_card in filter(lambda x: "attacks" not in x.keys(), pokemon_cards)]           


CARD_PATH = "data/cards/pokemon/sm10.json"
BASE_SET = "data/cards/sets/base1.json"


cm = CardManager(CARD_PATH)
# cm.change_set(BASE_SET)
cm_2 = CardManager(BASE_SET)

cm = cm + cm_2

return_raw_card_data = False

testing_cards = cm.get_cards_by_supertype("Pokemon", raw=False)

# for t_card in testing_cards:
#     print()
#     print(t_card.name)


# Deck Obj Testing
pokemon_cards = cm.get_cards_by_supertype("Pokemon", raw=return_raw_card_data)
energy_cards = cm.get_cards_by_supertype("Energy", raw=return_raw_card_data)
trainer_cards = cm.get_cards_by_supertype("Trainer", raw=return_raw_card_data)

downloader = Image_Downloader()


for i in range(0,1):
    card = pokemon_cards[i]
    url = card.image
    card_set = card.card_id[0:card.card_id.find("-")]
    name = slugify(card.card_id.replace(card_set + "-", "") + "-" + card.name) + ".png"
    downloader.download_image(url, card_set, name)
    sleep(2)
exit()

downloader = Image_Downloader()
url = pokemon_cards[0].image
name = "IMG-" + pokemon_cards[0].card_id + "-" + url[url.rfind("/")+1:]
downloader.download_image(url, name)

exit()

NUM_OF_TRAINER_CARDS_NEEDED = 6
NUM_OF_ENERGY_CARDS_NEEDED = 20
NUM_OF_POKEMON_CARDS_NEEDED = 14
TOTAL_NUM_OF_CARDS_NEEDED = NUM_OF_ENERGY_CARDS_NEEDED + NUM_OF_POKEMON_CARDS_NEEDED + NUM_OF_TRAINER_CARDS_NEEDED

num_of_trainer_cards = len(trainer_cards)
num_of_energy_cards = len(energy_cards)
num_of_pokemon_cards = len(pokemon_cards)


num_of_energy_cards_short = NUM_OF_ENERGY_CARDS_NEEDED - num_of_energy_cards

my_deck = Deck(pokemon_cards[0:NUM_OF_POKEMON_CARDS_NEEDED+num_of_energy_cards_short] + 
               energy_cards[0:NUM_OF_ENERGY_CARDS_NEEDED] + 
               trainer_cards[0:NUM_OF_TRAINER_CARDS_NEEDED])
# my_deck.display_deck()

print(my_deck)