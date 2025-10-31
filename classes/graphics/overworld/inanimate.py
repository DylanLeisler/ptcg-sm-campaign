import pygame
from dataclasses import dataclass
from ...entity import Entity
from ..sprite import VisualSprite

# pygame sprites need to be hashable. Decorating with dataclass normally overwrites __eq__ and custom __eq__ methods automatically set __hash__ to None
@dataclass(eq=False)
class Inanimate(Entity):
    
    def __init__(self, image: pygame.Surface, position: list[int]):
        super().__init__(VisualSprite(image, position))
        
        
    def __str__(self):
        return f"Inanimate(image:{self.sprite}, rect:{self.rect})"
    
