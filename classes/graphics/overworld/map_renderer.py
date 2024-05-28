from typing import Dict, List, Tuple
import pygame.Surface


class MapRenderer():
    """
    Utilizes a pygame surface (or 'screen') to parse instructions and display
    specified tiles from a tile map (or 'tile_sheet') based on the order specified
    in the instructions.
    """
    
    OFFSET = {'x': 0, 'y': 0}
    TILES = {}
  
    
    def __init__(self, screen: 'pygame.Surface', tile_sheet: Dict, instructions: Dict[str, List[List[str]]], dimensions: Tuple[int, int]):
        """
        Initializes the MapRenderer with the given screen, tile sheet, and instructions.
        Sets the screen dimensions according to the dimensions argument. The actual displaying
        of a tile occurs with the `execute_instructions` method.

        Args:
            screen (pygame.Surface): The display surface returned by pygame.display.set_mode,
            which should have dimensions equal to the 'DIMENSIONS' argument.
            
            tile_sheet (Dict): Dictionary of available tiles stored with relevant properties.
            The 'TILEMAP' property is required; it's value will be displayed as is.
            
            instructions (Dict[str, List[List[str]]]): The 'area' key should correspond with
            the directory the tiles are stored in. The 'specs' key is a list of rows, each
            a list of columns; they directly corresponds with what will appear on the screen
            and in what order. Each value should be the targeted key under LOCATION.<area>.TILES. 
            Each key represents a different tile object.
            
            dimensions (Tuple[int, int]): Must correspond to the dimensions used as an argument
            in pygame.display.set_mode upon the construction of 'screen'.
        """
        self.tile_sheet = tile_sheet
        self.set_instructions(instructions)
        self.screen = screen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = DIMENSIONS[0], DIMENSIONS[1]
        
    def set_instructions(self, instructions: Dict[str, List[list]]) -> 'Map_Renderer':
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

        


        
        
