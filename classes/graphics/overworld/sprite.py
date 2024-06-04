from time import sleep
from classes.graphics.logging import graphics_logger as log
import pygame


class Sprite():
    
    def __init__(self, sprite_surfaces: dict, position=[100,100], animation_speed=0.2):
        self.sprite = sprite_surfaces
        self.direction = "forward"
        self.current_frame = 0
        self.frame_time = 0
        self.animation_speed = animation_speed
        self.reverse = 1
        self.position = position
        
    def get_frame(self): 
        return self.sprite[self.direction][self.current_frame]
        
    def update(self, dt):
        self.frame_time += dt
        if self.frame_time >= self.animation_speed:
            self.frame_time = 0
            self._increment_frame()
            
    def _increment_frame(self):
        if self.reverse:
            self.current_frame -= 1
            if self.current_frame < 0:
                self.current_frame = 0
                self.reverse = False
        else:
            self.current_frame += 1
            if self.current_frame >= len(self.sprite[self.direction]):
                self.current_frame = len(self.sprite[self.direction])-1
                self.reverse = True
        log.debug(f"REVERSE: {self.reverse}")
        log.debug(f"CURR_FRAME: {self.current_frame}")
                
        
        