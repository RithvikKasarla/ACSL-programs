import deck
import game
import dealer
class player(object):
    """description of class"""
    def __init__(self,mydeck):
      self.d = mydeck
      self.hand = self.d.giveinitialcards()

    def max_card(self):
      return max(self.hand)

    def pick_a_card(self):
      self.hand.append(self.d.give_card())    
   
    def play_a_card(self):
      card_played = self.max_card()
      self.hand.remove(card_played)
      return card_played



