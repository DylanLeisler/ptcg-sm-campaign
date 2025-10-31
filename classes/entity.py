from typing import Self
import pygame
from .graphics.sprite import AnimatedSprite


# Refer to pygame Sprites as pygame.sprite.Sprite exclusively. Just 'Sprite' is a custom class for visual representation
# An entity is anything with a Sprite(I.E. Inanimates and Characters)
class Entity(pygame.sprite.Sprite):
    
    def __init__(self, sprite: AnimatedSprite):
        pygame.sprite.Sprite.__init__(self)
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
        return self.sprite.rect.topleft
        
    @position.setter
    def position(self, new_pos):
        self.sprite.rect.topleft = new_pos
        
    def update(self, delta_t, *args, **kwargs):
        self.sprite.update(delta_t, *args, **kwargs)
        
    def get_frame(self, *args, **kwargs):
        return self.sprite.get_frame(*args, **kwargs)
    
    @property
    def rect(self):
        return self.sprite.rect
    
    @rect.setter
    def rect(self, new_rect):
        self.sprite.rect = new_rect

    @property
    def image(self):
        return self.sprite.sprite
    
    @image.setter
    def image(self, new_image):
        self.sprite.sprite = new_image
        
    def add_to_group(self, groups: dict) -> Self:
        groups.setdefault(self.__class__.__name__.lower(), pygame.sprite.Group).add(self)
        return self
    
    def will_collide(self, dx, dy, groups):
        # Make a light, dynamic class that has the rect property for pygame's sprite.spritecollideany func.
        future = type("future_position", (), {"rect": self.rect.move(dx, dy)})()
        return self.is_colliding(groups, future)
        
    def is_colliding(self, groups, mover=None):
        if mover is None:
            mover = self
        if (s := pygame.sprite.spritecollideany(mover, groups["wall"])) is not None: # type: ignore
            # print(f"Collision detected between: {mover} and {s}\n\tMover coordinates at {mover.position}\n\tSprite coordinates at {s.position}")
            return True
        return False