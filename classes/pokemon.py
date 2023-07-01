from .card import Card
from .attack import Attack
from data.constants.energy import POKEMON as POKEMON_ENERGY_TYPES
from data.constants.card_properties import POKEMON as POKEMON_CARD_PROPS
from data.constants.optional_keys import POKEMON as POKEMON_OPTIONAL_KEYS


class Pokemon(Card):
    
    POSSIBLE_TYPES = POKEMON_ENERGY_TYPES
    POSSIBLE_PROPERTIES = POKEMON_CARD_PROPS
    OPTIONAL_KEYS = POKEMON_OPTIONAL_KEYS

    ENERGY_TYPES = POKEMON_ENERGY_TYPES

    CARD_PROPERTIES = POKEMON_CARD_PROPS

    OPTIONAL_KEYS = [
        ("flavorText", ""), ("abilities", [""]), ("evolvesFrom", [""]), 
        ("evolvesTo", [""]), ("level", ""), ("attacks", "")
        ]


    def __init__(self, name: str, card_id: str, super_type: str, energy_type: str, card_properties: list[str], 
                 description: str, pkmn_power: str, moves: list[Attack], evolvesFrom: str):

        super().__init__(name, card_id, super_type, card_properties, description)
        self.energy_type = energy_type
        # self.level = level
        self.pkmn_power = pkmn_power
        self.moves = moves
        self.evolvesFrom = evolvesFrom



    