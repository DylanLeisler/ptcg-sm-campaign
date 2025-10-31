from classes.card_manager import CardManager
# from classes.deck import Deck
from classes.characters.player import Player
from classes.graphics.sprite import AnimatedSprite
from classes.graphics.overworld.area import Area
from classes.graphics.tile_ingester import Tile_Ingester
from classes.graphics.overworld.sprite_map import SpriteMap
from classes.graphics.overworld.inanimate import Inanimate
from classes.image_downloader import Image_Downloader
from game_config import GameConfig as GC
import pygame


# CONSTANTS FOR TESTING
CARD_PATH = "data/cards/pokemon/sm10.json"
BASE_SET = "data/cards/sets/base1.json"

# Init
pygame.init()
screen = pygame.display.set_mode((GC.SCREEN_WIDTH, GC.SCREEN_HEIGHT))
pygame.display.set_caption("PTCG-SM-CAMPAIGN")
clock = pygame.time.Clock()
INANIMATE_TYPES = ["wall", "object", "floor"]

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

                # Main game loop          
def main(): 

    # Groups
    groups = {name: pygame.sprite.Group() for name in ["player", *INANIMATE_TYPES]}
    
    lab = Area(screen, lab_tiles, map_data, (GC.SCREEN_WIDTH, GC.SCREEN_HEIGHT), groups)
    
    player = make_player(GC.SPRITE_MAP_PATH, 
                         GC.ALPHA_COLOR_KEY,
                         (GC.SPRITE_LENGTH, GC.SPRITE_HEIGHT),
                         GC.LEFT_BORDER, 
                         GC.TOP_BORDER,
                         GC.BETWEEN_BORDER,
                         groups)
    
    last_movement_key = None
    key = None            
    running = True
    while running:
        dt = clock.tick(60)/1000 # 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render_map(lab)
         
        # TODO: Replace temporary implementation of last-key-wins movement up to two keys pressed with stack-based method
        key = pygame.key.get_pressed()
        ctx = (dt, groups)
        movement_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]
        movement_keys_pressed =  [k for k in movement_keys if key[k]]
        num_movement_keys_pressed = len(movement_keys_pressed)

        if num_movement_keys_pressed > 0:
            if num_movement_keys_pressed > 1:
                for pressed in movement_keys_pressed:
                    if pressed == last_movement_key:
                        continue
                    else:
                        player.move(pressed, *ctx)
                        break
            else:
                last_movement_key = movement_keys_pressed[0]
                player.move(movement_keys_pressed[0], *ctx)
    
            
        image = player.get_frame()

        screen.blit(image, player.position)
                
        # Update the display
        pygame.display.flip()
        

    # Clean up
    pygame.quit()

def make_player(path, alpha, dimensions, left_border, top_border, between_border, groups, animated_sprite_coords=GC.BASIC_ANIMATED_SPRITE_COORDS):
    sprite_handler = SpriteMap(path, 
                            transparent_color=alpha,
                            sprite_dimensions=dimensions,
                            left_border=left_border, 
                            top_border=top_border,
                            between_border=between_border)

    player_name = "Player"
    player_sprite = AnimatedSprite(
        sprite_handler.get_animated_sprite(*animated_sprite_coords),
        [100, 100])
    return Player(player_sprite, player_name).add_to_group(groups)
    # player.rect.update(player.rect.left, player.rect.top, player.rect.width, player.rect.height)


def render_map(area: Area):
    inanimates = area.get_inanimates()
    for inanimate in inanimates:
        screen.blit(inanimate.image, inanimate.position) 


def hidden():
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

if __name__ == "__main__":
    main()