from .card import Card
from data.constants.card_properties import TRAINER as TRAINER_CARD_PROPS
from data.constants.optional_keys import TRAINER as TRAINER_OPTIONAL_KEYS


class Trainer(Card):

    OPTIONAL_PROPERTIES = TRAINER_CARD_PROPS
    OPTIONAL_KEYS = TRAINER_OPTIONAL_KEYS


    def __init__(self, name: str, card_id: str, supertype: str, 
                 card_properties: list[str], description: str):

        super().__init__(name, card_id, supertype, card_properties, description)



    