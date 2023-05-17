from abc import ABC, abstractmethod

class Card(ABC):

    @abstractmethod
    def __init__(self, name: str, super_type: str, card_properties: list[str], 
                 description: str):

        self.name = name
        self.super_type = super_type
        self.card_properties = card_properties
        self.description = description



    