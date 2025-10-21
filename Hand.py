import pygame
import array as arr
from Globals import *
from Card import *
from Playerfield import *
from Sprites import *
from Deck import *
import assets

class Hand:
    def __init__(self, Y, CARDS):
        self.hand = []
        self.y = Y
    def display(self):
        # print("Display updated")
        increment = 550/(len(self.hand) + 1)
        for i in range(1, len(self.hand)+1):
            card_name = self.hand[i-1].get_name()
            # sprites[card_name].show(425 + i*175, self.y)
            sprites[card_name].show(625 + i*increment, self.y)
            # rect = pygame.Rect(625 + i*increment, self.y, 150, 225)
            if clicked():
                rect = sprites[card_name].get_rect()
                if rect.collidepoint(pygame.mouse.get_pos()):
                    print("Card clicked!")
                    return True
        return False

    def add_card(self, card):
        increment = 550/(len(self.hand) + 1)
        # self.number_of_cards += 1
        self.hand.append(card)
        self.display()
        # print(self.cards) # Prints out a non-empty list

    def get_cards(self):
        return self.hand

    # def get_number_of_cards(self):
    #     return self.number_of_cards

    # def transfer_card(self, player_field):
    #     success = False
    #     if len(self.removablecard) == 2:
    #         self.cards.pop(removablecard[1])
    #         for i in range(0,6):
    #             if success == False:
    #                 success = player_field.place_card(removablecard[0], i)