from time import sleep
from classes.utils.util_logging import graphics_logger as log
import pygame

class VisualSprite():
    
    def __init__(self, 
                 sprite_surface: pygame.Surface | dict, 
                 position: list[int] = [0, 0], 
                 direction: str = "forward"):
        self.sprite = sprite_surface
        self._direction = direction
        
        if isinstance(sprite_surface, pygame.Surface):
            rect = sprite_surface.get_rect()
            self.rect = pygame.rect.Rect(*position, rect.width, rect.height)
        # elif isinstance(sprite_dimensions, tuple):
        #     self.rect = pygame.rect.Rect(*position, *sprite_dimensions)
        elif isinstance(sprite_surface, dict):
            rect = sprite_surface[next(iter(sprite_surface))][0].get_rect()
            self.rect = pygame.rect.Rect(*position, rect.width, rect.height)
            
        # self.position = pygame.rect.Rect(*position, self.rect.width, self.rect.height)
            
    @property
    def position(self):
        return self.rect.topleft
    
    @position.setter
    def position(self, new_pos):
        self.rect.move_ip(*new_pos)
                
        

class AnimatedSprite(VisualSprite):
    
    def __init__(self, 
                 sprite_surface: dict[str, list[pygame.Surface]], 
                 position = [0, 0],  
                 direction: str = "forward",
                 animation_speed: float = 0.2):
        super().__init__(sprite_surface, position, direction)   
        self.current_frame = 0
        self.frame_time = 0
        self.animation_speed = animation_speed
        self.reverse = 1
        
    def get_frame(self): 
        return self.sprite[self._direction][self.current_frame]
        
    def update(self, dt, reset_frame=False):
        self.frame_time += dt
        if self.frame_time >= self.animation_speed:
            self.frame_time = 0
            if reset_frame:
                self.current_frame = 0
            else:
                self._increment_frame()
            
    def _increment_frame(self):
        if self.reverse:
            self.current_frame -= 1
            if self.current_frame < 0:
                self.current_frame = 0
                self.reverse = False
        else:
            self.current_frame += 1
            if self.current_frame >= len(self.sprite[self._direction]):
                self.current_frame = len(self.sprite[self._direction])-1
                self.reverse = True
        log.debug(f"REVERSE: {self.reverse}")
        log.debug(f"CURR_FRAME: {self.current_frame}")
    
    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self, direction):
        if not self.direction == direction:
            self.current_frame = 0
            self._direction = direction
                
        
        