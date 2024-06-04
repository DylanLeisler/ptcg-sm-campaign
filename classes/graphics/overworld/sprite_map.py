from typing import List
from classes.graphics.logging import graphics_logger as log
import pygame

 
class SpriteMap:    
    
    def __init__(self, sprite_map_path, transparent_color=None, sprite_dimensions=(0,0), left_border=0, top_border=0, right_border=0, bottom_border=0, between_border=0):
        """If initialized with a sprite_map_path, automatically loads it"""
        locals_copy = locals().copy()  # Make a copy of local variables to avoid modifying the actual locals during iteration
        for name, value in locals_copy.items():
            if name != 'self':
                setattr(self, name, value)
        self.load_map()
        
    def load_map(self):
        """Loads the map with pygame and converts the alpha"""
        self.sprite_map = pygame.image.load(self.sprite_map_path).convert()
        self.sprite_map.set_colorkey(self.transparent_color)
        
    def convert_to_list(self):
        """Make a list of sprites from the sprite sheet.
        """
        pass
    
    def get_sprite(self, x, y) -> pygame.Surface:
        """ Extracts and returns a single sprite from a sprite sheet. """
        
        #Surface that the selection of sprite map will be blitted on to
        sprite = pygame.Surface((self.sprite_dimensions[0], self.sprite_dimensions[1]), pygame.SRCALPHA)
        # sprite.blit(self.sprite_map, (0, 0), (x, y, self.sprite_dimensions[0], self.sprite_dimensions[1]))
        
        # Grabs sprite at x,y coord and blits it to Surface
        sprite.blit(self.sprite_map, (0, 0), (self.left_border + x*(self.sprite_dimensions[0]+self.between_border), 
                                              self.top_border + y*(self.sprite_dimensions[1]+self.between_border), 
                                              self.sprite_dimensions[0], 
                                              self.sprite_dimensions[1]))
        
        # Scales up Surface + Sprite blitted on to it
        sprite = pygame.transform.smoothscale(sprite, 
                                              (self.sprite_dimensions[0]*3, 
                                               self.sprite_dimensions[1]*3))
        return sprite
    
    def get_animated_sprite(self, forward: List[tuple], backward: List[tuple], left: List[tuple], right=None):
        if right is None:
            right=left
            #FLIP THEM!!
            
        args = locals()
        del args["self"]
        
        sprite = {}
        for direction,coords in args.items():
            sprite[direction] = [self.get_sprite(x,y) for x,y in coords]
            
        return sprite
        
        
    