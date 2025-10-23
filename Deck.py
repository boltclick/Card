import copy

from Card import *
from Globals import *
from Sprites import *

deck = []
sprites = {}
free_card = card("Free", "assets/Free.png", 1, 1, 0, "attack")
# free_card.Print()
A1 = card("A1", "assets/A1.png", 3, 1, 0, "attack")
A2 = card("A2", "assets/A2.png", 2, 4, 0, "attack")
A3 = card("A3", "assets/A3.png", 1, 4, 0, "attack")
A4 = card("A4", "assets/Letter.png", 3, 3, 0, "attack")
A5 = card("A5", "assets/A5.png", 2, 3, 0, "attack")
A6 = card("A6", "assets/A6.png", 3, 2, 0, "attack")
A7 = card("A7", "assets/A7.png", 2, 3, 0, "attack")
Catastrophe = card("Catastrophe", "assets/Catastrophe.png", 2, 5, 0, "attack")
deck += [free_card, A1, A2, A3, A4, A5, A6, A7, Catastrophe] # Adds all attack cards
S1 = card("S1", "assets/S1.png", 5, 1, 0, "support")
S2 = card("S2", "assets/S2.png", 4, 2, 0, "support")
S3 = card("S3", "assets/S3.png", 3, 1, 0, "support")
S4 = card("S4", "assets/S4.png", 5, 3, 0, "support") # iWhy is bro so strong
S5 = card("S5", "assets/S5.png", 6, 1, 0, "support")
S6 = card("S6", "assets/S6.png", 7, 0, 0, "support")
S7 = card("S7", "assets/S7.png", 4, 1, 0, "support")
S8 = card("S8", "assets/S8.png", 3, 1, 0, "support")
deck += [S1, S2, S3, S4, S5, S6, S7, S8]
P1 = card("P1", "assets/P1.png", 1, 0, 0, "passive")
P2 = card("P2", "assets/P2.png", 1, 0, 0, "passive")
P3 = card("P3", "assets/P3.png", 1, 0, 0, "passive")
P4 = card("P4", "assets/P4.png", 1, 0, 0, "passive")
deck += [P1, P2, P3, P4]
EA2 = card("EA2", "assets/EA2.png", 2, 4, 0, "attack")
Catastrophevil = card("Catastrophevil", "assets/Catastrophevil.png", 2, 5, 0, "attack")
ES4 = card("ES4", "assets/ES4.png", 5, 3, 0, "support") # Why is bro so strong
ES5 = card("ES5", "assets/ES5.png", 6, 1, 0, "support")
EP1 = card("EP1", "assets/EP1.png", 1, 0, 0, "passive")
EP2 = card("EP2", "assets/EP2.png", 1, 0, 0, "passive")
enemy_field = [EA2, Catastrophevil, ES4, ES5, EP1, EP2]
enemy_hand = [EA2, Catastrophevil, ES4, ES5, EP1, EP2]
# A2, Catastrophe, S4, S5, P1, P2
for c in deck:
    sprite_name = c.get_name()
    sprites[sprite_name] = Sprite(c)

for c in enemy_field:
    sprite_name = c.get_name()
    sprites[sprite_name] = Sprite(c)

print(sprites)