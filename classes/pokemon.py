from .card import Card
from .attack import Attack
from data.constants.energy_types import POKEMON as POKEMON_ENERGY_TYPES
from data.constants.card_properties import POKEMON as POKEMON_CARD_PROPS
from dataclasses import dataclass


@dataclass
class Pokemon(Card):

    ENERGY_TYPES = POKEMON_ENERGY_TYPES

    CARD_PROPERTIES = POKEMON_CARD_PROPS

    OPTIONAL_KEYS = [
        ("flavorText", ""), ("abilities", [""]), ("evolvesFrom", [""]), 
        ("evolvesTo", [""]), ("level", ""), ("attacks", "")
        ]


    def __init__(self, name: str, id: str, super_type: str, energy_type: str, card_properties: list[str], 
                 description: str, pkmn_power: str, moves: list[Attack], evolvesFrom: str):

        super().__init__(name, super_type, card_properties, description)
        self.energy_type = energy_type
        self.id = id
        # self.level = level
        self.pkmn_power = pkmn_power
        self.moves = moves
        self.evolvesFrom = evolvesFrom



    