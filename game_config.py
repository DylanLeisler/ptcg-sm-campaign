# Class for storing constants and configuration data core to the program, such as screen dimensions. Immutable.

from dataclasses import dataclass

@dataclass(frozen=True)
class GameConfig():
    
    SPRITE_MAP_PATH="data/overworld_sprites/alpha_sprite_map.png"
    
    BASE_SPRITE_DIMENSION = 16
    SPRITE_LENGTH = BASE_SPRITE_DIMENSION
    SPRITE_HEIGHT = BASE_SPRITE_DIMENSION
    SCALING_FACTOR = 4
    TILE_SIZE = BASE_SPRITE_DIMENSION*SCALING_FACTOR
    
    # Just have the values below immutable for testing/development. Consider it not fully implemented yet.
    MAP_WIDTH, MAP_HEIGHT = 8, 6
    SCREEN_WIDTH = MAP_WIDTH * TILE_SIZE 
    SCREEN_HEIGHT = MAP_HEIGHT * TILE_SIZE
    
    BASIC_ANIMATED_SPRITE_COORDS = ([(0,0),(1,0),(2,0)],
                            [(3,0),(4,0),(5,0)], 
                            [(6,0),(7,0)], 
                            [(8,0),(9,0)])
    
    # I actually don't remember exactly why these values are they are lol
    # TODO: Figure out why these values were set to these specific values and explain in comments
    ALPHA_COLOR_KEY = (255, 127, 39)
    TOP_BORDER = 34
    LEFT_BORDER = 9
    BETWEEN_BORDER = 1
    
    PLAYER_STARTING_POSITION = (100, 100)
    DEFAULT_MOVEMENT_DISTANCE_PER_FRAME = 2