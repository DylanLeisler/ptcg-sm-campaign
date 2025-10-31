import pygame
from dataclasses import dataclass



"""
    def __getitem__(self, key: str):
        return getattr(self, key)
        
Adding the method above will make key access work as member access. Good for variables.
"""

@dataclass
class AreaProp:
    type: str
    ext: str
    collision: bool
    short: str
    path: str
    image: pygame.Surface
    
    def __getitem__(self, key: str):
        return getattr(self, key)

@dataclass
class InanimateSpec:
    inanimate: AreaProp
    
    def __getitem__(self, key: str):
        return getattr(self, key)

@dataclass
class TileSheet:
    area: InanimateSpec
    
    def __getitem__(self, key: str):
        return getattr(self, key)
    