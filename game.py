import random

from roundresolver import RoundResolver


class Game:

    def __init__(self, player1, player2):
        self.board = ["B"]*7 + ["S"]*8 + ["X"]
        random.shuffle(self.board)

        self.rres = RoundResolver()

        self.p1 = player1
        self.p2 = player2

        self.players = [self.p1, self.p2]
        self.pi = 0
        self.player = self.players[self.pi]


    def main_loop(self):
        round_no = 1

        while ( len (self.board) > 1):
            #if round_no % 2 == 1:
            #    print("************ ROUND " + str(round_no/2 + 0.5) + " **********************")
            #print(self.board)
            self.rres.play_round(self.player, self.players, self.board)
            self.switch_player()

            round_no += 1

        if self.players[0].get_result() > self.players[1].get_result():
            return 1
        else:
            return 2

    def switch_player(self):
        self.pi = (self.pi + 1) % len (self.players)
        self.player = self.players[self.pi]




