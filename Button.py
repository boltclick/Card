import Deck
import pygame
import random as rnd
from Globals import *
from Hand import *
from Card import *
from Deck import *
player_hand = Hand(950, [])


class Button():
    def __init__(self, image, name):
        self.image = image
        self.name = name

    def show(self, x, y, width, height, pos, clicked):
        scaled = pygame.transform.scale(self.image, (width, height))
        screen.blit(scaled, (x, y))
        rect = pygame.Rect(x, y, width, height)
        # self.rect = scaled.get_rect()
        # self.rect.topleft = (x, y)
        #get mouse position
        #check mouseover and clicked conditions
        if rect.collidepoint(pos) and clicked:
            print('Button clicked!')
            if self.name == "Deck":
                rand = rnd.randint(0, len(deck) - 1)
                player_hand.add_card(deck[rand], clicked)
                # print(player_hand.get_cards()) # Prints out a non-empty list