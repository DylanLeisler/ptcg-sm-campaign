"""
Functions that help manage cards in PTCG-SM -- from data ingestion to data cleaning
also, fix this docstring color
"""

import json
import ast
from typing import Literal
from classes.pokemon import Pokemon, Attack
from classes.energy import Energy
from classes.trainer import Trainer


SUPERTYPE_SPELLING_VARIATIONS = {
    "Pokemon": ["PokÃ©mon", "Pokémon", "Pokemon"],
    "Energy": ["Energy"],
    "Trainer": ["Trainer"]
    }
POSSIBLE_SUPERTYPES = [SUPERTYPE for SUPERTYPE in SUPERTYPE_SPELLING_VARIATIONS.keys()]
FIND_AND_REPLACE_COMMON_VALUES = [("PokÃ©mon", "Pokemon"), ("Pokémon", "Pokemon")]


class CardManager(object):
    
    def __init__(self, path: str):
        """Requires a file path (either relative or absolute) to a JSON file
            containing the data that needs to be ingested."""
        self.path = path
        self.cleaned_data = self._clean_cards()
        self.cards = self.transform_card_data_types(self.cleaned_data)

    def __ingest_cards(func):
        """Decorator/Context Manager that opens collection of card data (JSON) and then passes
            it as an arg to the decorated function so that it may perform whatever witchcraft
            is needed.

        Args:
            func (function): Function should make use of the context created and managed by this
            decorator.
        """
        def context(self, *args, **kwargs):
            with open(self.path, "+r") as file:
                card_collection = json.loads(file.read())
                return func(*args, card_collection=card_collection)
        return context
    
    @__ingest_cards
    def _extract_data_by_supertype(supertype_option: Literal["Pokemon", "Energy", "Trainer"], card_collection=""):
        """Gets uncleaned card data by supertype. For internal use but can be used
            externally. The kwarg 'card_collection' is for use by the decorator."""
        if supertype_option in SUPERTYPE_SPELLING_VARIATIONS.keys():
            return [card_data for card_data in filter(lambda x: x["supertype"] in SUPERTYPE_SPELLING_VARIATIONS[supertype_option], card_collection)]
        else:
            # Throw error
            return "No matching supertype"
        
    def change_set(self, path: str):
        """Used to change the path of the CardManager object so it can ingest another set."""
        self.path = path
        self.cleaned_data = self._clean_cards()
        new_cards = self.transform_card_data_types(self.cleaned_data)
        for key in self.cards.keys():
            self.cards[key] += new_cards[key]
        
    def __add__(self, value):
        combined_cards = {}
        for key in self.cards:
            combined_cards[key] = self.cards[key] + value.cards[key]
        self.cards = combined_cards
        return self

    def get_cards_by_supertype(self, supertype_option: Literal["Pokemon", "Energy", "Trainer"], raw=False):
        """Gets properly typed cards, filtering by supertype."""   
        if raw == True:
            return self.cleaned_data[supertype_option]
        return self.cards[supertype_option]

    def _clean_cards(self) -> list:
        """Checks a list of keys (each key is the first value in a tuple,) each of which
            is expected in the card data object upon parsing. If the key isn't found, then
            they're added to the JSON data (memory, not the file itself,) and given an empty 
            value which corresponds with the type (str, list, dict...etc.) specified in the
            second value of the tuple. 
            For example: "" or [""]."""
        
        cards = {
            "Pokemon": self._extract_data_by_supertype("Pokemon"),
            "Energy": self._extract_data_by_supertype("Energy"),
            "Trainer": self._extract_data_by_supertype("Trainer")
        }
        clean_cards = {"Pokemon": [], "Energy": [], "Trainer": []}            
        
        for SUPERTYPE in POSSIBLE_SUPERTYPES:
            for unclean_card in cards[SUPERTYPE]:
                keyed_data = self.generalize_spelling(unclean_card, FIND_AND_REPLACE_COMMON_VALUES)
                cleaned_card = self.generalize_keys(keyed_data, globals()[SUPERTYPE].OPTIONAL_KEYS)
                clean_cards[SUPERTYPE].append(cleaned_card)       
        return clean_cards
    
    def transform_card_data_types(self, cleaned_data: list):
        return {
            "Pokemon": self._transform_pokemon_cards(cleaned_data["Pokemon"]),
            "Energy": self._transform_energy_cards(cleaned_data["Energy"]),
            "Trainer": self._transform_trainer_cards(cleaned_data["Trainer"])
        }
    
    def _transform_pokemon_cards(self, raw_data: list):
        return [Pokemon(card_data["name"],
                    card_data["id"], 
                    card_data["supertype"],
                    card_data["types"][0], 
                    card_data["subtypes"],
                    # card_data["level"],
                    card_data["flavorText"], 
                    card_data["abilities"][0], 
                    [Attack(attack) for attack in card_data["attacks"]], 
                    card_data["evolvesFrom"],
                    card_data["images"]["small"])
                    for card_data in raw_data]
        
    def _transform_energy_cards(self, raw_data: list):
        return [Energy(card_data["name"],
                    card_data["id"],
                    card_data["supertype"],
                    card_data["subtypes"],
                    card_data["rules"],
                    card_data["images"]["small"],
                    card_data["name"].split()[0] if card_data["supertype"] == "Basic" else "Colorless")
                    for card_data in raw_data]
        
    def _transform_trainer_cards(self, raw_data: list):
        return [Trainer(card_data["name"],
                    card_data["id"],
                    card_data["supertype"],
                    card_data["subtypes"],
                    card_data["rules"],
                    card_data["images"]["small"])
                    for card_data in raw_data]

    
    @staticmethod
    def generalize_keys(unclean_data: dict, optional_keys: list) -> dict:
        for key_tuple in optional_keys:
            if key_tuple[0] not in unclean_data.keys():
                unclean_data[key_tuple[0]] = key_tuple[1]
        return unclean_data

    @staticmethod
    def generalize_spelling(card_data: dict, find_and_replace: list) -> dict:
        """Performs find and replace on all values in dictionary: it converts the
            entire dictionary into a string with str(), performs the operations, and
            then uses the ast library to convert it back to a dict object before returning
            it."""
        str_card = str(card_data)
        for word_tuple in find_and_replace:
            str_card = str_card.replace(word_tuple[0], word_tuple[1])
        return ast.literal_eval(str_card)
    

               

if __name__ == '__main__':
    exit()  