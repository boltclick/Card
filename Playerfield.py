import numpy as np
from Globals import *
from Card import *
from Deck import *
from Hand import *

class Playerfield:
    def __init__(self, y):
        self.arr = np.empty(6, dtype=card)
        self.y = y
        self.xpos = [0, 250, 500, 750, 1000, 1250]
    # [P, P, S, A, A, S]


    def place_card(self, card, index):
        if (card.typing.name == "attack" and (index == 3 or index == 4)) or (card.typing.name == "support" and (index == 2 or index == 5)) or (card.typing.name == "passive" and (index == 0 or index == 1)):
            self.arr[index] = card
            # card.show(self.xpos[index], self.y)
            return True
        return False


