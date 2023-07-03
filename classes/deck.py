from .card import Card
from typing import List
import random
from classes.pokemon import Pokemon
from classes.energy import Energy
from classes.trainer import Trainer

class Deck(object):
    """Contains all NUM_OF_CARDS cards and their states at all times."""

    NUM_OF_CARDS = 40
    MAX_NUM_OF_IDENTICAL_CARDS = 3
    
    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.verify_num_of_cards()

    def verify_num_of_cards(self):
        num_of_cards = len(self.cards)
        if not num_of_cards == self.NUM_OF_CARDS:
            raise ValueError(f"Number of cards in deck: {num_of_cards}. Number required: {self.NUM_OF_CARDS}")
        
    def index_deck(self):
        card_index = {"Pokemon": [], "Energy": [], "Trainer": []}
        for card in self.cards:
            card_index[f"{type(card).__name__}"].append(f"{card.card_id}: {card.name}")
        return card_index
            
                
    def display_deck(self): 
        index = self.index_deck()    
        print(f"\nTotal Number of Cards in Deck: {len(self.cards)}")
        print("---------\n")
        print(f'  Pokemon: {len(index["Pokemon"])}')
        for card in index["Pokemon"]:
            print(f"    {card}")
        
    def get_card_count(self, supertype: str):
        card_index = {"Pokemon": [], "Energy": [], "Trainer": []}
        
    
    def shuffle(self):
        random.shuffle(self.cards)
