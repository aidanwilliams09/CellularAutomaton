import numpy as np

class OneDim:

    def __init__(self, x=100, y=200, ruleset=np.zeros((1, 8))):
        
        self.init_map(x, y, ruleset)

    def init_map(self, x, y, ruleset):
        self.x = x
        self.y = y
        self.ruleset = ruleset
        self.map = np.zeros((self.x, self.y), dtype=np.uint8)
        self.map[-1, self.y // 2] = 1

    def next_gen(self):
    
        triplets = [(4 * self.map[-1, i - 1], 2 * self.map[-1, i], self.map[-1, (i + 1) % self.y]) 
        for i in range(self.y)]

        new_gen = [self.ruleset[7 - sum(triplets[i])] for i in range(self.y)]

        self.map = np.delete(self.map, 0, 0)
        self.map = np.append(self.map, new_gen)
        self.map = np.reshape(self.map, (self.x, self.y))

    def get_map(self):
        return self.map * 255

    def reset(self):
        self.init_map(self.x, self.y, self.ruleset)

    def set_ruleset(self, ruleset):
        if ruleset != '':
            ruleset = int(ruleset)
            if ruleset < 256 and ruleset >= 0:
                rule = [int(b) for b in format(ruleset, 'b').zfill(8)]
                self.ruleset = np.array(rule)
