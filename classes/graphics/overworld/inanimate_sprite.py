import pygame
from dataclasses import dataclass

@dataclass
class InanimateSprite(pygame.sprite.Sprite):
    
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
    
