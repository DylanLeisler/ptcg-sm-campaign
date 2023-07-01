from abc import ABC, abstractmethod
from dataclasses import dataclass
from data.constants.supertypes import SUPERTYPES

@dataclass
class Card(ABC):
    
    POSSIBLE_TYPES = []
    POSSIBLE_SUPERTYPES = SUPERTYPES
    OPTIONAL_PROPERTIES = []
    OPTIONAL_KEYS = []

    @abstractmethod
    def __init__(self, name: str, card_id: str, super_type: str, card_properties: list[str], 
                 description: str):
        self.name = name
        self.card_id = card_id
        self.super_type = super_type
        self.card_properties = card_properties
        self.description = description



    