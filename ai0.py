import randomstub

# Dumbest AI of all, just picks the random chocolate
class AI0:

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
        r = randomstub.RandomStub().random_number(len(self.memory))
        #print("AI0 getting element: " + str(r), " memory lenght: " + str(len(self.memory)))
        return r