from classes.deck import Deck


class Card_Player:
    
    def __init__(self, name: str, deck: Deck, sprite):
        self.name = name
        self.deck = deck
        self.sprite = sprite
        pass

class Table():
    """This is the class that contains and manages all the components needed
        to conduct a card battle. It should contain two decks, prize areas,
        discard piles, active zones, passive zones, players, as well as 
        one stage slot.
    """
    
    def __init__(self, player: Card_Player, cpu: Card_Player):
        self.player = player
        self.cpu = cpu
        pass
    
    def initial_draw(self):
        # Perform this a number of times corresponding with a global and then
        #  add the returned values to the respective Card_Players hand.
        self.player.deck.draw_card() 
        pass
    
    