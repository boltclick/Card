import numpy as np
from Card import *
from Deck import *
class Playerfield:
    player_field = np.empty(6, dtype=card)
    # [P, P, S, A, A, S]
    def place_card(arr, card, index):
        if card.typing.name == "attack" and (index == 3 or index == 4):
            arr[index] = card
        elif card.typing.name == "support" and (index == 2 or index == 5):
            arr[index] = card
        elif card.typing.name == "passive" and (index == 0 or index == 1):
            arr[index] = card
        else:
            print("Error in placing card: Mismatched typing")
    place_card(player_field, Catastrophe, 3)
    print(player_field)
