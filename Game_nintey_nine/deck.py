class deck(object):
  def __init__(self, cards):
    self.CARDS_VALUE_DIC ={"T":"10", "J":"11", "Q" : "12", "K" : "13", "A" : "14"}
    self.cardvaldeck = []
    cards = cards.split(",")
    for x in cards:
      self.cardvaldeck.append(self.__get_card_value__(x) )
    self.score = self.cardvaldeck[0]
    self.cardvaldeck = self.cardvaldeck[1:]

  def give_card(self):
    card = self.cardvaldeck[0]
    self.cardvaldeck.pop(0)
    return card

  def __get_card_value__(self,card):
    if card in self.CARDS_VALUE_DIC:
      return int(self.CARDS_VALUE_DIC[card])
    else:
      return int(card)

  def giveinitialcards(self):
    hand = [self.cardvaldeck[0], self.cardvaldeck[1], self.cardvaldeck[2]]
    self.cardvaldeck = self.cardvaldeck[3:]
    return hand

  def get_score(self):
    return self.score


  #def find_card(self):
  #  self. card = self.cardvaldeck[0]
  #  self.cardvaldeck = self.cardvaldeck[1]

  #def give_initial_hand(self):
  #  return self.cardvaldeck[1:4]
  #def get_score():
  #  return self.score



