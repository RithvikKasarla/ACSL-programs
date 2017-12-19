import game
import dealer
import player
import deck
class main(object):
    """description of class"""



with open("gamedata.txt", "r") as f:
   lines = f.readlines()
lines = [l.replace('\n', '') for l in lines ]

for line in lines:
  g = game.game(line)
  g.play_game()
