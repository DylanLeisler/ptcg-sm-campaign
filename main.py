from classes.card_manager import CardManager
# from classes.deck import Deck
from classes.characters.character import Character
from classes.graphics.sprite import AnimatedSprite
from classes.graphics.overworld.area import Area
from classes.graphics.tile_ingester import Tile_Ingester
from classes.graphics.overworld.sprite_map import SpriteMap
from classes.graphics.overworld.inanimate import Inanimate
from classes.image_downloader import Image_Downloader
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
INANIMATE_TYPES = ["wall", "object", "floor"]

# Groups
groups = {name: pygame.sprite.Group() for name in ["player", *INANIMATE_TYPES]}

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

lab = Area(screen, lab_tiles, map_data, (SCREEN_WIDTH, SCREEN_HEIGHT), groups)


transparent_color = (255, 127, 39)
top_border = 34
left_border = 9
between_border = 1
sprite_length = 16
sprite_height = 16
animated_sprite_coords = ([(0,0),(1,0),(2,0)],
                         [(3,0),(4,0),(5,0)], 
                         [(6,0),(7,0)], 
                         [(8,0),(9,0)])

sprite_handler = SpriteMap(SPRITE_MAP_PATH, 
                           transparent_color=transparent_color,
                           sprite_dimensions=(sprite_length, sprite_height),
                           left_border=left_border, 
                           top_border=top_border,
                           between_border=1)

player_name = "Player"
player_sprite = AnimatedSprite(
    sprite_handler.get_animated_sprite(*animated_sprite_coords),
    [100, 100])
player = Character(player_sprite, player_name)
# player.rect.update(player.rect.left, player.rect.top, player.rect.width, player.rect.height)

groups["player"].add(player)

                # Main game loop          
def main():             
    running = True
    while running:
        dt = clock.tick(60)/1000 # 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render_map(lab)
        
        key = pygame.key.get_pressed()
        dist = 2 # distance moved in 1 frame
        if key[pygame.K_DOWN]: # down key
            player.direction = "forward"
            player.position = (player.position[0], player.position[1] + dist) # move down
            player.update(dt)
        elif key[pygame.K_UP]: # up key
            player.direction = "backward"
            player.position = (player.position[0], player.position[1] - dist) # move up
            player.update(dt)
        elif key[pygame.K_RIGHT]: # right key
            player.direction = "right"
            player.position = (player.position[0] + dist, player.position[1]) # move right
            player.update(dt)
        elif key[pygame.K_LEFT]: # left key
            player.direction = "left"
            player.position = (player.position[0] - dist, player.position[1]) # move left
            player.update(dt)
        else:
            player.update(dt, reset_frame=True)
        
            
        image = player.get_frame()

        screen.blit(image, player.position)
        
        if (s := pygame.sprite.spritecollideany(player, groups["wall"])) is not None: # type: ignore
            print(f"Collision detected between: {player} and {s}\n\tPlayer coordinates at {player.position}\n\tSprite coordinates at {s.position}")
                
        # Update the display
        pygame.display.flip()
        

    # Clean up
    pygame.quit()


def render_map(area: Area):
    inanimates = area.get_inanimates()
    for inanimate in inanimates:
        screen.blit(inanimate.sprite.sprite, inanimate.position) 


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