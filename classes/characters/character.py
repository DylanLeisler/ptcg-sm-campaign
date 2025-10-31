import pygame
from ..entity import Entity



class Character(Entity):
        
    def __init__(self, sprite, name, starting_position=None):
        super().__init__(sprite)
        self.name = name
        self.position = starting_position