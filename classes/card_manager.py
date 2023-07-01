"""
Functions that help manage cards in PTCG-SM -- from data ingestion to data cleaning
also, fix this docstring color
"""

import json
from typing import Literal
from classes.pokemon import Pokemon, Attack
from classes.energy import Energy


SUPERTYPE_SPELLING_VARIATIONS = {
    "Pokemon": ["PokÃ©mon", "Pokémon", "Pokemon"],
    "Energy": ["Energy"],
    "Trainer": ["Trainer"]
    }
POSSIBLE_SUPERTYPES = [SUPERTYPE for SUPERTYPE in SUPERTYPE_SPELLING_VARIATIONS.keys()]


class CardManager(object):
    
    def __init__(self, path: str):
        """Requires a file path (either relative or absolute) to a JSON file
            containing the data that needs to be ingested."""
        self.path = path
        self.cards = self._clean_cards()

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
    def _extract_data_by_supertype(supertype_option: Literal["Pokemon, Energy, Trainer"], card_collection=""):
        """Gets uncleaned card data by supertype. For internal use but can be used
            externally. The kwarg 'card_collection' is for use by the decorator."""
        if supertype_option in SUPERTYPE_SPELLING_VARIATIONS.keys():
            return [card_data for card_data in filter(lambda x: x["supertype"] in SUPERTYPE_SPELLING_VARIATIONS[supertype_option], card_collection)]
        else:
            # Throw error
            return "No matching supertype"

    def get_cards_by_supertype(self, supertype_option: Literal["Pokemon, Energy, Trainer"], raw=False):
        """Gets properly typed cards, filtering by supertype."""
        if not supertype_option in SUPERTYPE_SPELLING_VARIATIONS.keys():
            # Throw error
            return "No matching supertype"
        
        if raw == True:
            return self.cards[supertype_option]
        
        if supertype_option == "Pokemon":
            return [Pokemon(card_data["name"],
                card_data["id"], 
                card_data["supertype"],
                card_data["types"][0], 
                card_data["subtypes"],
                # card_data["level"],
                card_data["flavorText"], 
                card_data["abilities"][0], 
                [Attack(attack) for attack in card_data["attacks"]], 
                card_data["evolvesFrom"])
                for card_data in self.cards["Pokemon"]]
        elif supertype_option == "Energy": 
            return [Energy(card_data["name"],
                        card_data["id"],
                        card_data["supertype"],
                        card_data["subtypes"],
                        card_data["rules"],
                        card_data["name"].split()[0] if card_data["supertype"] == "Basic" else "Colorless")
                        for card_data in self.cards["Energy"]]
        elif supertype_option == "Trainer":
            return True
        else:
            return False

    def _clean_cards(self) -> list:
        """Checks a list of keys (each key is the first value in a tuple,) each of which
            is expected in the card data object upon parsing. If the key isn't found, then
            they're added to the JSON data (memory, not the file itself,) and given an empty 
            value which corresponds with the type (str, list, dict...etc.) specified in the
            second value of the tuple. 
            For example: "" or [""]."""
        cards = {}
        cards["Pokemon"] = self._extract_data_by_supertype("Pokemon")
        cards["Energy"] = self._extract_data_by_supertype("Energy")
        clean_cards = {"Pokemon": [], "Energy": [], "Trainer": []}
        
        for unclean_card in cards["Pokemon"]:
            for key_tuple in Pokemon.OPTIONAL_KEYS:
                if key_tuple[0] not in unclean_card.keys():
                    unclean_card[key_tuple[0]] = key_tuple[1]
                    cleaned_card = unclean_card
            clean_cards["Pokemon"].append(cleaned_card)
            
        for unclean_card in cards["Energy"]:
            for key_tuple in Energy.OPTIONAL_KEYS:
                if key_tuple[0] not in unclean_card.keys():
                    unclean_card[key_tuple[0]] = key_tuple[1]
                    cleaned_card = unclean_card
            clean_cards["Energy"].append(cleaned_card)
            
        return clean_cards
        
    def get_pokemon_cards(self, raw=False):
        """Grabs every card from the JSON path that has a supertype of 'Pokemon.'

        Args:
            raw (bool, optional): Setting 'raw' to True will return the unformatted JSON data.
            The value False will convert the data and return it as 'Pokemon' objects, a 
            Defaults to False.

        Returns:
            _type_: _description_
        """

        
        

if __name__ == '__main__':
    exit()


    