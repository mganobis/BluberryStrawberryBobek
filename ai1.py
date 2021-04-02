import randomstub

# AI picks the "right" chocolate if it has been unveiled, otherwise picks the random one
class AI1:

    def __init__(self):
        self.memory = ["?"]*16

    def reset(self):
        self.memory = ["?"] * 16

    def update_picked_chocolate(self, i):
        del self.memory[i]

    def update_unveiled_chocolate(self, i, t):
        self.memory[i] = t

    def update_bobek(self, ret):
        self.memory = ["?"]*len(self.memory)
        if ret != None:
            self.memory.append("?")

    # HERE AI WORKS
    def choose_chocolate(self, die):
        r = 0
        try:
            r = self.memory.index(die) # if there is an unveiled chocolate of this type, pick it
        except ValueError: # there isn't known chocolate of this type on the board
            r = randomstub.RandomStub().random_number(len(self.memory))
        #print("AI1 getting element: " + str(r))
        return 0