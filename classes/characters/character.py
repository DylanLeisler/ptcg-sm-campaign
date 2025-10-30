import pygame
from ..entity import Entity



class Character(Entity):
        
    def __init__(self, sprite, name):
        super().__init__(sprite)
        self.name = name