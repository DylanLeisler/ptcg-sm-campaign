from random import randint
from classes.deck import Deck, Card
from classes.card_player import CardPlayer
from ..data.constants.game_instance import STARTING_HAND_SIZE


class GameInstance():
    """This is the class that contains each card battle. It must be passed both
        the player and the cpu opponent. It will copy each respective card player
        and then perform all needed computations (particularly involving the decks) 
        using the copies.
    """
    
    def __init__(self, player: CardPlayer, cpu: CardPlayer):
        self.player = player # Remember: these function as if they're pass by value
        self.cpu = cpu       #  Not pass by reference!
        self.BOTH_PLAYERS = [self.player, self.cpu]
        
        self.initial_draw()
        #Verify at least one basic, non-trainer pokemon card in hand
        #Place active pokemon
        #Place bench pokemon
        self.determine_first_turn()
        #Cycle through phases
    
    def initial_draw(self):
        """Initalizes hand properter for both players in instance. Then uses 
            draw_cards to draw STARTING_HAND_SIZE num of cards into both hands.
        """
        self.player.hand = []
        self.cpu.hand = []
        
        self.draw_cards(self.BOTH_PLAYERS, n=STARTING_HAND_SIZE)
        
    def choose_heads_or_tails() -> bool:
        #get user input through widget
        user_input = 0
        return user_input
    
    def coin_flip():
        return randint(0, 1)
    
    def determine_first_turn(self):
        return self.player if self.choose_heads_or_tails() == self.coin_flip() else self.cpu
        
        
    def draw_card(targ: CardPlayer):
        if len(targ.deck > 0):
            targ.hand.append(targ.deck.cards.pop())
        else:
            #Throw game over flag
            pass
        
    def draw_cards(self, targs: list[CardPlayer], n=1):
        """Accepts list of targets and uses draw_card n number of times on each
            target. If n is a list, targs[x] will draw n[x] cards, so they're
            sizes must be equal.

        Args:
            targs (list(CardPlayer)): List of players to draw cards.
            
        Optional:
            n (int, list(int)): Number of cards each target will draw. If list, 
                each value specifies number of cards the corresponding targ will
                draw. Default 1 (int). 
        """
        if type(n) == list(int):
            for targ, i in targs, n:
                while i > 0:
                    self.draw_card(targ)
                    i -= 1
        elif type(n) == int:
            for targ in targs:
                while n > 0:
                    self.draw_card(targ)
                    n -= 1
    
    