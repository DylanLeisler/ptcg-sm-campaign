from unittest import TestCase
from unittest import main as begin_test
from classes.deck import Deck
from classes.pokemon import Pokemon
from classes.attack import Attack

class TestDeck(TestCase):

    dummy_cards = ""

    def setUp(self):

        with open("data/cards/energy_types.json", "r+") as file:
            for x in range(1, Deck.NUM_OF_CARDS + 1):
                dummy_cards = Pokemon(f"test_card_{x}", f"test-set-{x}", "Pokemon", 
                                      Pokemon.ENERGY_TYPES[x % len(Pokemon.ENERGY_TYPES)],
                                      Pokemon.CARD_PROPERTIES[x % len(Pokemon.CARD_PROPERTIES)],
                                      f"test_description_{x}", f"test_pkmn_power_{x}", 
                                      [Attack({
                                            "name": "test_attack_1",
                                            "damage": f"test_damage_{x}",
                                            "cost": ["Grass"],
                                            "convertedEnergyCost": 3,
                                            "description": f"Test attack description number {x}"
                                            })],
                                      "test_pokemon"
                                    )
        
    def test_make_deck(self):
        self.working_deck = Deck(self.dummy_cards)
        self.assertIsInstance(self.working_deck, Deck)


if __name__ == '__main__':
    begin_test()