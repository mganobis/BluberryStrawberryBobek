import random

import randomstub

class Player:

    def __init__(self, n, ai):
        self.name = n
        self.ai = ai
        self.picked_chocolates = []

    def reset(self):
        self.picked_chocolates = []
        self.ai.reset()

    def choose_chocolate(self, die): # TODO this is a stub, AI goes here
        return self.ai.choose_chocolate(die)

    def pick_chocolate(self, c):
        self.picked_chocolates.append(c)

    def return_chocolate(self):
        if len(self.picked_chocolates) > 0:
            p = randomstub.RandomStub().random_number(len(self.picked_chocolates))
            r = self.picked_chocolates[p]
            del self.picked_chocolates[p]
            return r
        else:
            return None

    def get_result(self):
        return (len(self.picked_chocolates))

    def update_ai(self, event_type, die, picked, index, returned):
        if event_type == "MATCH":
            self.ai.update_picked_chocolate(index)
        elif event_type == "NOMATCH":
            self.ai.update_unveiled_chocolate(index, picked)
        elif event_type == "BOBEK":
            self.ai.update_bobek(returned)
        else:
            raise ValueError
