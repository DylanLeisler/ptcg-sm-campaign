from classes.card_manager import CardManager
# from classes.deck import Deck
from classes.image_downloader import Image_Downloader
from classes.draw_map import Draw_Map
from classes.map_ingester import Map_Ingester
import json
import pygame

#TODO: handle missing key exceptions
# moveless_pokemon = [pokemon_card for pokemon_card in filter(lambda x: "attacks" not in x.keys(), pokemon_cards)]           


CARD_PATH = "data/cards/pokemon/sm10.json"
BASE_SET = "data/cards/sets/base1.json"

pygame.init()

TILE_SIZE = 16*4
MAP_WIDTH, MAP_HEIGHT = 5, 6
SCREEN_WIDTH, SCREEN_HEIGHT = MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile Map Game")


map_renderer = Draw_Map()
# map_renderer.load_tiles_by_location("lab")

map_ingester = Map_Ingester()
map_ingester.build_index()

# Sample map layout: a list of strings or numbers indicating tiles
map_data = [
    ["top_left", "top_center", "top_center", "top_center", "top_right"],
    ["side_center", "bottom_center", "bottom_center", "bottom_center", "side_center"],
    ["side_center", "floor", "floor", "floor", "side_center"],
    ["side_center", "floor", "floor", "floor", "side_center"],
    ["bottom_left", "bottom_floor", "bottom_floor", "bottom_floor", "bottom_right"],
    ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "bottom_center"],
    ["bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow"]
]

# map_data = [
#     ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "top_right"],  # Each number corresponds to a tile
#     ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "top_right"],
#     ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "top_right"],
#     ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "top_right"],
#     ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "top_right"],
# ]

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Draw the tile map
#     TOTAL_OFF_SET = {"h": 0, "v": 0}
#     for row_index, row in enumerate(map_data):
#         for col_index, tile in enumerate(row):
#             tile_key = "WALLS"
#             key = map_data[row_index][col_index]
#             if key == "floor":
#                 tile_key = "FLOORS"
#             image = map_renderer.TILES[tile_key][key]
#             screen.blit(image, (TOTAL_OFF_SET["h"], TOTAL_OFF_SET["v"]))
#             image_width, image_height = image.get_size()
#             TOTAL_OFF_SET["h"] += image_width
#             if col_index == (len(row)-1):
#                 TOTAL_OFF_SET["v"] += image_height
#                 TOTAL_OFF_SET["h"] = 0

#     # Update the display
#     pygame.display.flip()

# # Clean up
# pygame.quit()

# print(map_renderer.TILES)

exit()


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

downloader.download_images(pokemon_cards)
downloader.download_image(energy_cards)


###

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