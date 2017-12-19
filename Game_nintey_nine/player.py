import deck
import game
import dealer
class player(object):
    """description of class"""
    def __init__(self,mydeck):
      self.d = mydeck
      self.hand = self.d.giveinitialcards()

    def play_a_card(self):
      card_played = max(self.hand)
      self.hand.remove(card_played)
      return card_played
    def pick_a_card(self):
      self.hand.append(self.d.give_card())

