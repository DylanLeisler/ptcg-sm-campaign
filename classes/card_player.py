from classes.deck import Deck


class CardPlayer:
    
    def __init__(self, name: str, deck: Deck, sprite):
        self.name = name
        self.deck = deck
        self.sprite = sprite