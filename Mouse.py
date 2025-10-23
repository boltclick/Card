import pygame
from Card import *
from Playerfield import *
from Globals import *
from Hand import *
from Button import *


# Track mouse click state
# mouse_down = False
# selected_card = None
# selected_card_index = None

# def select_card_from_hand(hand, pos):
#     #checks if the mouse click is on any card in the hand
#
#     global selected_card, selected_card_index
#
#     if selected_card is not None:
#         # Already have a selected card, do nothing here
#         print("card already selected, skipping selection")
#         return
#
#     #len returns the number of cards in players hand
#     print(len(hand.get_cards()))
#     #iterate over all cards in hand to check for click collisions
#     for i in range(1, len(hand.get_cards()) + 1):
#         card_name = hand.cards[i - 1].get_name()
#         # Assuming sprites[card_name].show(...) already called elsewhere for drawing
#         rect = pygame.Rect(625 + i * increment, hand.y, 150, 225)
#
#         if rect.collidepoint(pos) and clicked():
#             print(f"Mouse over card {card_name} at position {rect.topleft}")
#             selected_card = hand.cards[i - 1] #set the selected card
#             selected_card_index = i - 1       #Store its index in hand
#             print(f"Selected card: {selected_card.get_name()}")
#             break

def place_card_on_field(field, hand, pos, clicked): # If you need to detect a click, add a parameter called "clicked", and then use the var clicked from the main class to fill it, when called there
    if hand.display(clicked):
        index = hand.get_selected()[0]
        card = hand.get_selected()[1]
        if player.get_tenergy() != 0 or card.get_name() == "Free":

            # card = card_sprite.get_card()
            # print(hand.get_selected())
            # return hand.get_selected()
            # count = 0
            for i in range(0,6):
                if (card.get_typing() == "passive" and i in (0,1) and field.get_field()[i] == None) or (card.get_typing() == "support" and i in (2,5) and field.get_field()[i] == None) or (card.get_typing() == "attack" and i in (3,4) and field.get_field()[i] == None):
                    print("Card moved to field")
                    field.place_card(card, i)
                    hand.remove_card(card)
                    if card.get_name() != "Free":
                        player.change_tenergy(-1)
                    return
                # if i == None:
                #     print(count)
                    # if (card.get_typing() == "passive" and (i in (0, 1))) or (card.get_typing() == "support" and (i in (2, 5))) or (card.get_typing() == "attack" and (i in (3, 4))):
                    #     field.place_card(card, index)