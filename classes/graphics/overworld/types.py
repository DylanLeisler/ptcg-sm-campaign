import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, image, position, group):
        super().__init__()
        self.image = image  # Load the image and convert it
        self.rect = self.image.get_rect(topleft=position)  # Position the sprite
        group.add(self)
        

class Floor(pygame.sprite.Sprite):
    def __init__(self, image, position, group):
        super().__init__()
        self.image = image  # Load the image and convert it
        self.rect = self.image.get_rect(topleft=position)  # Position the sprite
        group.add(self)   


class Object(pygame.sprite.Sprite):
    def __init__(self, image, position, group):
        super().__init__()
        self.image = image  # Load the image and convert it
        self.rect = self.image.get_rect(topleft=position)  # Position the sprite
        group.add(self)
        
        
