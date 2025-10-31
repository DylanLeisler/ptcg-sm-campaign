from typing import Self
import pygame
from .graphics.sprite import AnimatedSprite, VisualSprite



# An entity is anything with a sprite (I.E. Inanimates and Characters)
class Entity(pygame.sprite.Sprite):
    
    def __init__(self, sprite: AnimatedSprite | VisualSprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = sprite
        if not isinstance(self.sprite.rect, pygame.rect.Rect):
            raise Exception(f"got {type(self.sprite.rect)}")
        self.collision_rect = self.sprite.rect.copy()
        if not isinstance(self.collision_rect, pygame.rect.Rect):
            raise Exception(f"got2 {type(self.collision_rect)}")

    @property
    def direction(self):
        return self.sprite.direction
    
    @direction.setter
    def direction(self, cardinal_direction):
        self.sprite.direction = cardinal_direction

    @property
    def collision_position(self):
        return self.collision_rect.topleft
        
    @collision_position.setter
    def collision_position(self, new_pos):
        # self.sprite.rect.move(*new_pos)
        self.collision_rect.move_ip(*new_pos)
        
    @property
    def visual_position(self):
        return self.sprite.position
    
    @visual_position.setter
    def visual_position(self, new_pos):
        self.sprite.position = new_pos
        
    @property
    def position(self):
        return self.visual_position
    
    @position.setter
    def position(self, new_pos):
        self.visual_position = new_pos
        self.collision_position = new_pos
        
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
        future = type("future_position", (), {"rect": self.collision_rect.move(dx, dy)})()
        return self.is_colliding(groups, future)
        
    def is_colliding(self, groups, mover=None):
        if mover is None:
            mover = self
        if (s := pygame.sprite.spritecollideany(mover, groups["wall"])) is not None: # type: ignore
            # print(f"Collision detected between: {mover} and {s}\n\tMover coordinates at {mover.position}\n\tSprite coordinates at {s.position}")
            return True
        return False