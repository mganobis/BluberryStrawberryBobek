import randomstub

class RoundResolver:

    def play_round(self, active_player, players, board):
        d = randomstub.RandomStub().roll_dice()

        c = active_player.choose_chocolate(d)

        #print("on die: " + d)
        if (d == board[c]):
            #print("match!")
            for p in players:
                p.update_ai("MATCH", d, board[c], c, None)
            active_player.pick_chocolate(d)
            del board[c]

        elif (board[c] == "X"):  # BOBEK
            #print("bobek!")
            r = active_player.return_chocolate()
            for p in players:
                p.update_ai("BOBEK", d, board[c], c, r)
            if r != None:
                board.append(r)
            randomstub.RandomStub().shuffle_list(board)
        else:
            #print("no match!")
            for p in players:
                p.update_ai("NOMATCH", d, board[c], c, None)