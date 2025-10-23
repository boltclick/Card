import numpy as np
from Globals import *
from Card import *
from Deck import *
from Hand import *

class Playerfield:
    def __init__(self, y, passive_offset = 0):
        self.arr = np.empty(6, dtype=card)
        # self.y = y
        self.ypos = [y+25+passive_offset, y+200+passive_offset, y, y, y, y]
        self.xpos = [225, 225, 500, 750, 1000, 1250]
    # [P, P, S, A, A, S]


    def place_card(self, card, index):
        if (card.get_typing() == "passive" and (index == 0 or index == 1)) or (card.get_typing() == "support" and (index == 2 or index == 5)) or (card.get_typing() == "attack" and (index == 3 or index == 4)):
            self.arr[index] = card
            sprites[card.get_name()].show(self.xpos[index], self.ypos[index])
            if card.get_typing() == "passive":
                sprites[card.get_name()].rotate_90()
            # card.show(self.xpos[index], self.y)
            return True
        return False

    def show_field(self):
        for i in range(0,6):
            if self.arr[i] != None:
                if self.arr[i].get_hp() <= 0:
                    self.arr[i] = None
                else:
                    sprites[self.arr[i].get_name()].show(self.xpos[i], self.ypos[i])


    def get_field(self):
        return self.arr
