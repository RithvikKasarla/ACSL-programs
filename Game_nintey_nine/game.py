import player
import deck
import dealer

class game(object):
    """description of class"""
    def __init__(self, pack_of_cards):
      self.mydeck = deck.deck(pack_of_cards)
      self.points = self.mydeck.get_score()
      self.p = player.player(self.mydeck)
      self.dealer = dealer.dealer( self.mydeck)

    def update_points(self, card):
      if card == 14:
        if self.points + 14 > 99:
          card = 1
      if card == 9:
        card = 0
      if card == 10:
        card = -10
      self.points = self.points + card

    def is_gameover(self):
      return self.points > 99

    def play_game(self):
      while self.is_gameover() == False:
        self.update_points(self.p.play_a_card())
        self.p.pick_a_card()
        if self.is_gameover() == True:
          print(self.points, " dealer")
          return
        else:
          self.update_points(self.dealer.play_a_card())
          if self.is_gameover() == True:
            print(self.points, " player")
            return            

