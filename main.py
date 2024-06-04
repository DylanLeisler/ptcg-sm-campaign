from classes.card_manager import CardManager
# from classes.deck import Deck
from classes.image_downloader import Image_Downloader
from classes.graphics.overworld.map_renderer import MapRenderer
from classes.graphics.tile_ingester import Tile_Ingester
from classes.graphics.overworld.sprite_map import SpriteMap
from classes.graphics.overworld.sprite import Sprite
import pygame

#TODO: handle missing key exceptions
# moveless_pokemon = [pokemon_card for pokemon_card in filter(lambda x: "attacks" not in x.keys(), pokemon_cards)]           

SPRITE_MAP_PATH="data/overworld_sprites/alpha_sprite_map.png"

CARD_PATH = "data/cards/pokemon/sm10.json"
BASE_SET = "data/cards/sets/base1.json"

TILE_SIZE = 16*4
MAP_WIDTH, MAP_HEIGHT = 8, 6
SCREEN_WIDTH, SCREEN_HEIGHT = MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile Map Game")

clock = pygame.time.Clock()


#map_renderer = Draw_Map()
#map_renderer.load_tiles_by_location("lab")

map_ingester = Tile_Ingester()
# map_ingester.get_index()
map_ingester.build_index()\
            # .print_index()

# Sample map layout: a list of strings or numbers indicating tiles
# map_data = {"area": "LAB", 
#             "specs": [
#     ["top_left", "top_center", "top_center", "top_center", "top_right"],
#     ["side_center", "bottom_center", "bottom_center", "bottom_center", "side_center"],
#     ["side_center", "floor", "floor", "floor", "side_center"],
#     ["side_center", "floor", "floor", "floor", "side_center"],
#     ["bottom_left", "bottom_floor", "bottom_floor", "bottom_floor", "bottom_right"],
#     ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "bottom_center"],
#     ["bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow"]
# ]}

map_data = {"area": "LAB", 
            "specs": [
    ["top_left", "top_center", "top_center", "top_center", "top_center", "top_center", "top_center", "top_right"],
    ["side_center", "bottom_center", "bottom_center", "bottom_center","bottom_center", "bottom_center", "bottom_center", "side_center"],
    ["side_center", "floor", "floor", "floor", "floor", "floor", "floor", "side_center"],
    ["side_center", "floor", "floor", "floor", "floor", "floor", "floor", "side_center"],
    ["bottom_left", "bottom_floor", "bottom_floor", "bottom_floor", "bottom_floor", "bottom_floor", "bottom_floor", "bottom_right"],
    ["bottom_center", "bottom_center", "bottom_center", "bottom_center", "bottom_center", "bottom_center", "bottom_center", "bottom_center"],
    ["bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow", "bottom_shadow"]
]}

map_renderer = MapRenderer(screen, map_ingester.get_index(), map_data, (SCREEN_WIDTH, SCREEN_HEIGHT))

transparent_color = (255, 127, 39)
top_border = 34
left_border = 9
between_border = 1
sprite_length = 16
sprite_height = 16

sprite_handler = SpriteMap(SPRITE_MAP_PATH, 
                           transparent_color=transparent_color,
                           sprite_dimensions=(sprite_length, sprite_height),
                           left_border=left_border, 
                           top_border=top_border,
                           between_border=1)


player_sprite = Sprite(
    sprite_handler.get_animated_sprite(
        [(0,0),(1,0),(2,0)],
        [(3,0),(4,0),(5,0)], 
        [(6,0),(7,0)], 
        [(8,0),(9,0)]
        )
    )

                # Main game loop          
                
running = True
while running:
    dt = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    map_renderer.execute_instructions()
    
    key = pygame.key.get_pressed()
    dist = 2 # distance moved in 1 frame
    if key[pygame.K_DOWN]: # down key
        player_sprite.position[1] += dist # move down
    elif key[pygame.K_UP]: # up key
        player_sprite.position[1] -= dist # move up
    if key[pygame.K_RIGHT]: # right key
        player_sprite.position[0] += dist # move right
    elif key[pygame.K_LEFT]: # left key
        player_sprite.position[0] -= dist # move left
       
        
    player_sprite.update(dt)
    image = player_sprite.get_frame()

    screen.blit(image, player_sprite.position)
            
    # Update the display
    pygame.display.flip()
    

# Clean up
pygame.quit()

exit()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

    # Draw the tile map
    TOTAL_OFF_SET = {"h": 0, "v": 0}
    for row_index, row in enumerate(map_data):
        for col_index, tile in enumerate(row):
            tile_key = "WALLS"
            key = map_data[row_index][col_index]
            if key == "floor":
                tile_key = "FLOORS"
            image = map_renderer.TILES[tile_key][key]
            screen.blit(image, (TOTAL_OFF_SET["h"], TOTAL_OFF_SET["v"]))
            image_width, image_height = image.get_size()
            TOTAL_OFF_SET["h"] += image_width
            if col_index == (len(row)-1):
                TOTAL_OFF_SET["v"] += image_height
                TOTAL_OFF_SET["h"] = 0

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()

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