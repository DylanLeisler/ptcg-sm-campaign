from .card import Card
from typing import List
import random

class Deck(object):
    "Contains all NUM_OF_CARDS cards and their states at all times. Should be a component of the CardCollection class."

    NUM_OF_CARDS = 40
    MAX_NUM_OF_IDENTICAL_CARDS = 3
    
    def __init__(self, cards: List[Card]):
        self.verify_num_of_cards(cards)
        self.cards = cards

    def verify_num_of_cards(self):
        num_of_cards = len(self.cards)
        if not num_of_cards == self.NUM_OF_CARDS:
            raise ValueError(f"Number of cards in deck: {num_of_cards}. Number required: {self.NUM_OF_CARDS}")
    
    def shuffle(self):
        random.shuffle(self.cards)

    def get_card_map(self):
        map_of_cards = dict()
        for card in self.cards:
            key = card.supertype + "".join([subtype for subtype in card["subtypes"].sort()])
            if not key in map_of_cards.keys():
                map_of_cards[key] = 1
            else:
                map_of_cards[key] += 1
