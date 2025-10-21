import pygame
from Card import *
from Playerfield import *
from Globals import *
from Hand import *
from Button import *


# Track mouse click state
mouse_down = False
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

def place_card_on_field(field, hand, pos):
    if hand.display():
        print(hand.get_cards())
        return hand.get_card()
    # if player_hand.display() != []:
        # selected_card_index = player_hand.display()[0]
        # selected_card = player_hand.display()[0]
        # print(selected_card_index)
        # print(selected_card)

    #
    #
    # # var = player_field.display()
    # # var[0] = index; var[1] = card
    # # print("Card is placed in " + var[0] + "slot")
    # selected_card = player_hand.display()
    # # print(selected_card)
    # if selected_card is None:
    #     return  # No card selected
    #
    # if clicked():  # Left mouse clicked
    #     print(selected_card)
    #     mx, my = pos #mouse x, mouse y
    #     print(pos)
    #
    #     # Loop through each field index
    #     for idx in range(6):  # 6 field slots, idx gives current pos in loop
    #         rect_x = player_field.xpos[idx]
    #         rect = pygame.Rect(rect_x, player_field.y, 150, 225)
    #
    #         # If mouse is over this field rectangle
    #         if rect.collidepoint(mx, my):
    #
    #             # Try to place the card
    #             success = player_field.place_card(selected_card, idx)
    #
    #             if success:
    #                 print(f"Card placed in slot {idx}")
    #                 # Remove from hand?
    #                 hand.cards.pop(selected_card_index)
    #                 # Clear selection
    #                 selected_card = None
    #                 selected_card_index = None
    #             else:
    #                 print("Invalid slot for this card type.")
    #
    #             break  # Only try one slot per click