from typing import Self
from classes.graphics.logging import graphics_logger as log
import pygame
 

class SpriteHandler:
    
    
    def __init__(self, sprite_map_path=""):
        self.sprite_map_path = sprite_map_path
        if sprite_map_path:
            self.load_map(sprite_map_path)
        
    def load_map(self, sprite_map_path):
        self.sprite_map = pygame.image.load(sprite_map_path).convert_alpha()
        
    def set_num_of_sprites(self, x: int, y: int) -> Self:
        self.set_num_of_sprites = set(x,y)
        return Self
        
    def calc_sprite_size(self: set):
        if not self.set_num_of_sprites:
            #throw error
            log("Must set number of sprites before calc can occur.")
        map_height = self.sprite_map.get_height()
        map_width = self.sprite_map.get_width()
        return set(
            int(map_width/self.num_of_sprites_x_y[0]),
            int(map_height/self.num_of_sprites_x_y[1])
        )
        
    def convert_to_list(self):
        
        
    