from .card import Card
from .attack import Attack
from dataclasses import dataclass

@dataclass
class Pokemon(Card):

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



    