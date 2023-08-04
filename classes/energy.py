from .card import Card
from typing import Literal
from data.constants.energy import ENERGY as ENERGY_CARD_ENERGY_TYPES
from data.constants.card_properties import ENERGY as ENERGY_CARD_PROPS
from data.constants.optional_keys import ENERGY as ENERGY_OPTIONAL_KEYS


class Energy(Card):

    POSSIBLE_TYPES = ENERGY_CARD_ENERGY_TYPES
    OPTIONAL_PROPERTIES = ENERGY_CARD_PROPS
    OPTIONAL_KEYS = ENERGY_OPTIONAL_KEYS


    def __init__(self, name: str, card_id: str, supertype: str, 
                 card_properties: list[str], description: str, image: str, energy_type: Literal["Pokemon", "Energy", "Trainer"]):

        super().__init__(name, card_id, supertype, card_properties, description, image)
        self.energy_type = energy_type



    