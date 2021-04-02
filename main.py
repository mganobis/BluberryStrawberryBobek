
from game import Game
from ai0 import AI0
from ai1 import AI1
from player import Player

p1 = 0
p2 = 0

player1 = Player("P1", AI1())
player2 = Player("P2", AI0())

for i in range(1000):
    player1.reset()
    player2.reset()
    g = Game(player1, player2)
    r = g.main_loop()
    if r == 1:
        p1 +=1
    if r == 2:
        p2 +=1

print("RESULT: Player1=" + str(p1) +" ,Player2=" + str(p2))