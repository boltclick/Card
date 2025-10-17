from Card import *
# #Let's move everything under here to a different file, so we can have all the display stuff here
deck = []
free_card = card("Free Card", 1, 1)
# free_card.Print()
A1 = card("A1", 3, 1)
A2 = card("A2", 2, 4)
A3 = card("A3", 1, 4)
A4 = card("A4", 3, 3)
A5 = card("A5", 2, 3)
A6 = card("A6", 3, 2)
A7 = card("A7", 2, 3)
Catastrophe = card("Catastrophe", 1, 5)
deck += [free_card, A1, A2, A3, A4, A5, A6, A7, Catastrophe] # Adds all attack cards
S1 = card("S1", 5, 1, Typing("support"))
S2 = card("S2", 4, 2, Typing("support"))
S3 = card("S3", 3, 1, Typing("support"))
S4 = card("S4", 5, 3, Typing("support")) # Why is bro so strong
S5 = card("S5", 6, 1, Typing("support"))
S6 = card("S6", 7, 0, Typing("support"))
S7 = card("S7", 4, 1, Typing("support"))
S8 = card("S8", 3, 1, Typing("support"))
deck += [S1, S2, S3, S4, S5, S6, S7, S8]
P1 = card(P1, 0, 0, Typing("Passive"))
P2 = card(P2, 0, 0, Typing("Passive"))
P3 = card(P3, 0, 0, Typing("Passive"))
P4 = card(P4, 0, 0, Typing("Passive"))
deck += [P1, P2, P3, P4]
enemy_deck = deck
# for i in deck:
#     print(i.name)
# print("\n\n")
# for i in deck:
#     i.Print()
#     print("")