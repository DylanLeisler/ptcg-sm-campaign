"""
Functions that help manage cards in PTCG-SM -- from data ingestion to data cleaning
also, fix this docstring color
"""

import json
import sys
from pathlib import Path
from classes.pokemon import Pokemon, Attack


POKEMON_SPELLING_VARIATIONS = ["PokÃ©mon", "Pokémon", "Pokemon"]

class CardManager(object):
    
    def __init__(self, path: str):
        """Requires a file path (either relative or absolute) to a JSON file
            containing the data that needs to be ingested."""
        self.path = path
        self.cards = self._clean_pokemon_cards()

    def __ingest_cards(func):
        """Decorator/Context Manager that pulls collection of card data (JSON) and then passes
            it as an arg to the decorated function.

        Args:
            path (str): _description_
        """
        def context(self, *args, **kwargs):
            with open(self.path, "+r") as file:
                card_collection = json.loads(file.read())
                return func(*args, card_collection=card_collection)
        return context

    @__ingest_cards
    def _get_raw_cards_by_supertype(supertype: str, card_collection=""):
        """Gets uncleaned cards by supertype. For internal use but can be used
            externally. The karg 'card_collection' is for use by the decorator."""
        if supertype == "Pokemon":
            return [pokemon_card for pokemon_card in filter(lambda x: x["supertype"] in POKEMON_SPELLING_VARIATIONS, card_collection)]
        else:
            return "No matching supertype"

    def _clean_pokemon_cards(self) -> list:
        """Checks a list of keys (each key is the first value in a tuple)
            needed in the respective object. If the key isn't found, then
            they're added and given an empty value with the correct type
            (which is contained in the second value of the tuple.) For example
            "" or [""]."""
        cards = self._get_raw_cards_by_supertype("Pokemon")
        clean_cards = []
        for unclean_card in cards:
            for key_tuple in Pokemon.OPTIONAL_KEYS:
                if key_tuple[0] not in unclean_card.keys():
                    unclean_card[key_tuple[0]] = key_tuple[1]
            clean_cards.append(unclean_card)
        return {"Pokemon": clean_cards}
        
    def get_pokemon_cards(self, raw=False):
        if raw == True:
            return self.cards["Pokemon"]
        else:
            formatted_cards = [Pokemon(card_data["name"],
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
            return formatted_cards
        
        

if __name__ == '__main__':
    exit()


    