import pygame
from .sprite import Sprite


# Refer to pygame Sprites as pygame.sprite.Sprite exclusively. Just Sprite is a custom class
class Entity(pygame.sprite.Sprite):
    
    def __init__(self, name, sprite: Sprite):
        self.name = name
        self.sprite = sprite
    
    # Property + setter redirects player.direction calls to player.sprite.direction
    # Only one source of truth + sprite has special setter instructions
    @property
    def direction(self):
        return self.sprite.direction
    
    @direction.setter
    def direction(self, cardinal_direction):
        self.sprite.direction = cardinal_direction

    # When assigning to entity.position, it will call the setter.
    # However, when assigning to entity.position[n], this will actually only call the getter,
    #  which will return a reference. 
    # The list should mutate fine, but remember the setter will *not* be called when indexing. 
    @property
    def position(self):
        return self.sprite.position
        
    @position.setter
    def position(self, new_pos):
        self.sprite.position = new_pos
        
    def update(self, delta_t):
        self.sprite.update(delta_t)