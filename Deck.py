from Card import *
from Globals import *
from Sprites import *

deck = []
sprites = {}
free_card = card("Free", "assets/McMissing.png", 1, 1)
# free_card.Print()
A1 = card("A1", "assets/A1.png", 3, 1)
A2 = card("A2", "assets/A2.png", 2, 4)
A3 = card("A3", "assets/A3.png", 1, 4)
A4 = card("A4", "assets/Letter.png", 3, 3)
A5 = card("A5", "assets/A5.png", 2, 3)
A6 = card("A6", "assets/A6.png", 3, 2)
A7 = card("A7", "assets/A7.png", 2, 3)
Catastrophe = card("Catastrophe", "assets/Catastrophe.png", 1, 5)
deck += [free_card, A1, A2, A3, A4, A5, A6, A7, Catastrophe] # Adds all attack cards
S1 = card("S1", "assets/S1.png", 5, 1, Typing("support"))
S2 = card("S2", "assets/S2.png", 4, 2, Typing("support"))
S3 = card("S3", "assets/S3.png", 3, 1, Typing("support"))
S4 = card("S4", "assets/S4.png", 5, 3, Typing("support")) # Why is bro so strong
S5 = card("S5", "assets/S5.png", 6, 1, Typing("support"))
S6 = card("S6", "assets/S6.png", 7, 0, Typing("support"))
S7 = card("S7", "assets/S7.png", 4, 1, Typing("support"))
S8 = card("S8", "assets/S8.png", 3, 1, Typing("support"))
deck += [S1, S2, S3, S4, S5, S6, S7, S8]
P1 = card("P1", "assets/P1.png", 0, 0, Typing("Passive"))
P2 = card("P2", "assets/P2.png", 0, 0, Typing("Passive"))
P3 = card("P3", "assets/P3.png", 0, 0, Typing("Passive"))
P4 = card("P4", "assets/P4.png", 0, 0, Typing("Passive"))
deck += [P1, P2, P3, P4]
enemy_deck = deck

for c in deck:
    sprite_name = c.get_name()
    sprites[sprite_name] = Sprite(c.get_image())

print(sprites)