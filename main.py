import inspect
from typing import Dict, TypedDict
from classes.card_manager import CardManager
# from classes.deck import Deck
from classes.image_downloader import Image_Downloader
from classes.graphics.overworld.map_renderer import MapRenderer
from classes.graphics.tile_ingester import Tile_Ingester
from classes.graphics.overworld.sprite_map import SpriteMap
from classes.graphics.overworld.sprite import Sprite
import pygame

# CONSTANTS

CARD_PATH = "data/cards/pokemon/sm10.json"
BASE_SET = "data/cards/sets/base1.json"

SPRITE_MAP_PATH="data/overworld_sprites/alpha_sprite_map.png"
TILE_SIZE = 16*4
MAP_WIDTH, MAP_HEIGHT = 8, 6
SCREEN_WIDTH, SCREEN_HEIGHT = MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE


# Init

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PTCG-SM-CAMPAIGN")
clock = pygame.time.Clock()


# Groups

player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
floor_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()
lab_group = pygame.sprite.Group()



## Pre-Loop Setup ##

# Use instructions to ingest pngs
lab_tiles = Tile_Ingester()\
                    .build_index()\
                    .get_index()

# Visual definition of lab set up
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

class AreaProps(TypedDict):
    TYPE: str
    EXT: str
    COLLISION: bool
    SHORT: str
    PATH: str
    IMAGE: pygame.Surface
 
    
class Area():
    
    def __init__(self, area_index: Dict[str, Dict[str, AreaProps]]):
        self.area_name = list(area_index.keys())[0]
        assert self.area_name == "LAB"
        self.sprites = {}
        self._ingest_tiles(area_index[self.area_name])
        
    def _ingest_tiles(self, tiles):
        from classes.graphics.overworld import types as sprite_types_module
        classes = [member for name, member in inspect.getmembers(sprite_types_module)
            if inspect.isclass(member) and member.__module__ == sprite_types_module.__name__]
        sprite_types = [(cls.__name__, cls) for cls in classes]
        
        for key,tile in tiles.items():
            for sprite_type in sprite_types:
                if tile["TYPE"] == sprite_type[0].upper():
                    group = globals()[f"{sprite_type[0].lower()}_group"]
                    new_sprite = sprite_type[1](tile["IMAGE"], (0,0), group)
                    self.sprites[key] = new_sprite
                    
                    
                
        
lab = Area(lab_tiles)
print(lab.sprites)
exit()

map_renderer = MapRenderer(screen, lab_tiles, map_data, (SCREEN_WIDTH, SCREEN_HEIGHT))

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

# player_group.add(player_sprite)

                # Main game loop          
                
running = True
while running:
    dt = clock.tick(60)/1000 # 60 frames per second
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    map_renderer.execute_instructions()
    
    key = pygame.key.get_pressed()
    dist = 2 # distance moved in 1 frame
    if key[pygame.K_DOWN]: # down key
        player_sprite.direction = "forward"
        player_sprite.position[1] += dist # move down
        player_sprite.update(dt)
    elif key[pygame.K_UP]: # up key
        player_sprite.direction = "backward"
        player_sprite.position[1] -= dist # move up
        player_sprite.update(dt)
    elif key[pygame.K_RIGHT]: # right key
        player_sprite.direction = "right"
        player_sprite.position[0] += dist # move right
        player_sprite.update(dt)
    elif key[pygame.K_LEFT]: # left key
        player_sprite.direction = "left"
        player_sprite.position[0] -= dist # move left
        player_sprite.update(dt)
    else:
        player_sprite.update(dt, reset_frame=True)
       
        
    image = player_sprite.get_frame()

    screen.blit(image, player_sprite.position)
    
    if pygame.sprite.spritecollideany(player_sprite, wall_group):
        print("Collision detected!")
            
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