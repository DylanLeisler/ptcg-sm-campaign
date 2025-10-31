import pygame
from models import TileSheet 
from typing import List, Tuple, TypedDict
from .inanimate import Inanimate
from ...utils.util_logging import graphics_logger as log
#classes.utils.util_logging import graphics_logger as log

log.setLevel("WARNING")


class InstructionsType(TypedDict):
    area: str
    specs: List[List[str]]

class Area():
    """
    Utilizes a pygame surface (or 'screen') to parse instructions and display
    specified tiles from a tile map (or 'tile_sheet') based on the order specified
    in the instructions.
    """
    
    OFFSET = {'x': 0, 'y': 0}
    TILES = {}
  
    
    def __init__(self, screen: 'pygame.Surface', tile_sheet: TileSheet, instructions: InstructionsType, DIMENSIONS: Tuple[int, int], groups):
        """
        NEEDS TO BE UPDATED
        Initializes the MapRenderer with the given screen, tile sheet, and instructions.
        DIMENSIONS should match actual dimensions used for construction of screen. The 
        displaying of tiles occurs with the `execute_instructions` method.

        Args:
            screen (pygame.Surface): The display surface returned by pygame.display.set_mode,
            which should have dimensions equal to the 'DIMENSIONS' argument.
            
            tile_sheet (Dict): Dictionary of available tiles stored with relevant properties.
            The 'TILEMAP' property is required; it's value will be displayed as is.
            
            instructions (Dict[str, List[List[str]]]): The 'area' key should correspond with
            the directory the tiles are stored in. The 'specs' key is a list of rows, each
            a list of columns; they directly correspond with what will appear on the screen
            and in what order. Each value should be the targeted key under LOCATION.<area>.TILES. 
            Each key represents a different tile object.
            
            dimensions (Tuple[int, int]): Must correspond to the dimensions used as an argument
            in pygame.display.set_mode upon the construction of 'screen'.
        """
        self.tile_sheet = tile_sheet
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = DIMENSIONS
        self.groups = groups
        self.area = instructions["area"]
        self.specs = instructions["specs"]
        
        self._init_inanimate_categories()
        try:
            self._init_inanimates(self.specs)
        except TypeError as e:
            raise TypeError(
                f"{e}\n{type(self.specs)} passed to self._ingest_tiles. Contents are:\n{self.specs}")

    def _init_inanimate_categories(self):
        """ Ingest all the tiles for the respective Area.
        Loops through every tile k:v and calls internal methods _classify_sprites and _ingest_sprites

        Args:
            tiles (dict): Tiles from Tile_Ingester. 
                          Key is item ("chair", "wall", etc.) and the value is the AreaProp
        """
        self.inanimate_categories = {}    
        for inanimate_cat, tile in self.tile_sheet[self.area].items():
            self.inanimate_categories.setdefault(inanimate_cat, []).append(tile['TYPE'].lower())
            
    def _init_inanimates(self, map_data):
        self.inanimates = []
        for row_id, row in enumerate(map_data):
            for col_id, col in enumerate(row):
                tiles = self.tile_sheet[self.area.upper()]
                image = tiles[col]["IMAGE"]
                new_sprite = Inanimate(image, 
                                       (Area.OFFSET["x"], Area.OFFSET["y"])) # type: ignore
                new_sprite.position = new_sprite.sprite.position
                self.inanimates.append(new_sprite)
                self.add_sprite_to_group(tiles[col]["TYPE"].lower(), new_sprite)
                offset = [False, False]
                if col_id == (len(row) - 1):
                    offset[0] = True
                    if row_id == (len(map_data) - 1):
                        offset[1] = True
                self._adjust_offset(image.get_size(), offset)
              
    def add_sprite_to_group(self, sprite_type: str, sprite):
        self.groups[sprite_type].add(sprite)
        return self 
    
    def _adjust_offset(self, tile_dimensions, axis_reset) -> 'Area':
        image_width, image_height = tile_dimensions[0], tile_dimensions[1]
        
        if axis_reset[0]:
            self.reset_offset("x")
            Area.OFFSET["y"] += image_height
            log.debug(f"\nIMAGE_HEIGHT: {image_height}\n\tMAP_REND.OFFSET[y]: {Area.OFFSET['y']}")
        else:
            Area.OFFSET["x"] += image_width
            
        if axis_reset[1]:
            self.reset_offset("y")
            pass
  
        return self

    def reset_offset(self, axis) -> 'Area':
        Area.OFFSET[axis] = 0
        return self
    
    def get_inanimates(self):
        return self.inanimates
    
if __name__ == '__main__':
    exit()

        


        
        
