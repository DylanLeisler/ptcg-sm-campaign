from .card import Card
from typing import List
import random
from classes.pokemon import Pokemon
from classes.energy import Energy
from classes.trainer import Trainer
from ..data.constants.deck import DECK_SIZE, MAX_REPEATING_CARDS

class Deck(object):
    """Contains all DECK_SIZE cards and their states at all times."""

    # These are defined here so they can be overwritten by an inheriting class
    #  if needed, while still using self to refer to them.
    DECK_SIZE = DECK_SIZE
    MAX_REPEATING_CARDS = MAX_REPEATING_CARDS
    
    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.verify_num_of_cards()

    def verify_num_of_cards(self):
        num_of_cards = len(self.cards)
        if not num_of_cards == self.DECK_SIZE:
            raise ValueError(f"Number of cards in deck: {num_of_cards}. Number required: {self.DECK_SIZE}")
        
    def index_deck(self):
        card_index = {"Pokemon": [], "Energy": [], "Trainer": []}
        for card in self.cards:
            card_index[f"{type(card).__name__}"].append(f"{card.card_id}: {card.name}")
        return card_index       
                
    def display_deck(self): 
        index = self.index_deck()    
        print(f"\nTotal Number of Cards in Deck: {len(self.cards)}")
        print("---------\n")
        for supertype in ["Pokemon", "Energy", "Trainer"]:   
            print("=====\n")
            print(f'  {supertype}: {len(index[supertype])}\n')
            for card in index[supertype]:
                print(f"    {card}")
            print()
        
    def get_card_count(self, supertype: str):
        card_index = {"Pokemon": [], "Energy": [], "Trainer": []}     
    
    def shuffle(self):
        random.shuffle(self.cards)
