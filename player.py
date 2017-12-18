class player(object):
    """description of class"""
    def __init__(self, hand):
      if type(hand) == bytearray and len(hand) == 3:
        self.hand = hand
    def playcard(self):

