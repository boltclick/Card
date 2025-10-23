import pygame
import random as rnd
from Globals import *
from Hand import *
from Card import *
from Deck import *
from Player import *
player = Player(30, 3)
enemy = Player(30, 3)
player_hand = Hand(825, [])
enemy_field = Playerfield(250, -100)
enemy_field.place_card(EP1, 0); enemy_field.place_card(EP2, 1); enemy_field.place_card(ES4, 2)
enemy_field.place_card(EA2, 3); enemy_field.place_card(Catastrophevil, 4); enemy_field.place_card(ES5, 5)
player_field = Playerfield(575)



class Button():
    def __init__(self, image, name, turn):
        self.image = image
        self.name = name
        self.turn = turn

    def show(self, x, y, width, height, pos, clicked, player_hand, player_field, enemy_field = None):
        scaled = pygame.transform.scale(self.image, (width, height))
        screen.blit(scaled, (x, y))
        rect = pygame.Rect(x, y, width, height)
        # self.rect = scaled.get_rect()
        # self.rect.topleft = (x, y)
        #get mouse position
        #check mouseover and clicked conditions
        if rect.collidepoint(pos) and clicked: # Drew needs to be a peramater
            print('Button clicked!')
            if self.name == "Deck" and self.turn == 0:
                rand = rnd.randint(0, len(deck) - 1)
                failing = True
                player_field_counter = 0
                available_card_counter = 0
                for i in range(0,6):
                    if player_field.get_field()[i] != None:
                        player_field_counter += 1
                for card in deck:
                    if card.get_hp() > 0:
                        available_card_counter += 1
                if player_field_counter + len(player_hand.get_cards()) >= available_card_counter:
                    failing = False
                while failing: # Check if hand + deck = cards with more than 0 hp
                    if deck[rand] not in player_hand.get_cards() and deck[rand] not in player_field.get_field() and deck[rand].get_hp() > 0:
                        player_hand.add_card(deck[rand], clicked)
                        failing = False
                    rand = rnd.randint(0, len(deck) - 1)
                    # player_hand.add_card(deck[rand], clicked)
                    # self.turn += 1
                # print(player_hand.get_cards()) # Prints out a non-empty list
            if self.name == "End Turn":
                self.turn = 0
                player.change_tenergy(1)
                print(player_field.get_field())
                for i in range(0, 6):
                    player_card = player_field.get_field()[i]
                    print(player_card)
                    enemy_card = enemy_field.get_field()[i]
                    print(enemy_card)
                    if player_card != None and enemy_card != None:
                        print("Card damaged")
                        player_card.take_damage(enemy_card.get_atk())
                        enemy_card.take_damage(player_card.get_atk())

                    elif player_card == None and enemy_card != None:
                        print("Player damaged")
                        player.damage(enemy_card.get_atk())
                    elif player_card != None and enemy_card == None:
                        enemy.damage(player_card.get_atk())