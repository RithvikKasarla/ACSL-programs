import game
import player
import deck

class dealer(object):
    def __init__(self, cardDeck):
      self.deck = cardDeck
    """description of class"""

    def play_a_card(self):
      return self.deck.give_card()

