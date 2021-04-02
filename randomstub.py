import random

class RandomStub:

    def random_number(self, n):
        return random.randrange(n)

    def shuffle_list(self, l):
        return random.shuffle(l)

    def roll_dice(self):
        return random.choice(["B","S"])
