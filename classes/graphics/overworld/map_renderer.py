from asyncio import sleep
import time
from typing import Dict
import pygame
import json


class Map_Renderer():
    """Checks tile_sheet arg for key name and then uses pygame to 
    display contents of "TILEMAP" child-key. Will read instructions
    passed to it (json) to establish order and quantity of objects.

    """
    
    OFFSET = {'x': 0, 'y': 0}
    TILES = {}
  
    
    def __init__(self, tile_sheet: dict, instructions: Dict[str, list], DIMENSIONS: set, screen):
        self.tile_sheet = tile_sheet
        self.set_instructions(instructions)
        self.screen = screen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = DIMENSIONS[0], DIMENSIONS[1]
        # self.init_display()

    # def set_display(self, screen: pygame.display.set_mode):
    #     # Set up the display
    #     self.screen = pygame.display.set_mode((Map_Renderer.SCREEN_WIDTH, Map_Renderer.SCREEN_HEIGHT))
    #     pygame.display.set_caption("Tile Map Game")
        
    def set_instructions(self, instructions: Dict[str, list]) -> 'Map_Renderer':
        self.area = instructions["area"]
        self.specs = instructions["specs"]
        return self
    
    # def _load_instructions(self, instructions_json) -> List[list]:
    #     return json.load(instructions_json)
    
    def execute_instructions(self) -> 'Map_Renderer':
        for row_id,row in enumerate(self.specs):
            for tile_id,tile in enumerate(row):
                tilemap = self.tile_sheet[self.area]["TILES"][tile]["TILEMAP"]
                # print(tile)
                #time.sleep(1)
                #print(f"\tTILE_ID: {tile_id}\n\tROW_ID: {row_id}")
                
                self._render_tile(tilemap)
                # print(Map_Renderer.OFFSET)
                
                offset = [False, False]
                if tile_id == (len(row) - 1):
                    offset[0] = True
                    if row_id == (len(self.specs) - 1):
                        offset[1] = True  
                self._adjust_offset(tilemap.get_size(), offset)
                
        return self   
    
    def _render_tile(self, tile):
        self.screen.blit(tile, (Map_Renderer.OFFSET["x"], Map_Renderer.OFFSET["y"]))
        return self
    
    def _adjust_offset(self, tile_dimensions, axis_reset) -> 'Map_Renderer':
        image_width, image_height = tile_dimensions[0], tile_dimensions[1]
        
        if axis_reset[0]:
            self.reset_offset("x")
            Map_Renderer.OFFSET["y"] += image_height
            # print(f"\nIMAGE_HEIGHT: {image_height}\n\tMAP_REND.OFFSET[y]: {Map_Renderer.OFFSET['y']}")
        else:
            Map_Renderer.OFFSET["x"] += image_width
            
        if axis_reset[1]:
            self.reset_offset("y")
            pass
  
        return self

    def reset_offset(self, axis) -> 'Map_Renderer':
        Map_Renderer.OFFSET[axis] = 0
        return self
    
if __name__ == '__main__':
    exit()

        


        
        
