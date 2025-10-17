# Card cat = new Card (HP, ATK, TYPE, ABILITY)

class Typing: #This shouldn't be a subclass because it's general
    def __init__(self, NAME = "attack"):
        self.name = NAME

class Ability: # Idk if ability needs to use hp, atk, etc. of the parent card. If it doesn't, than this shouldn't be a subclass
    def __init__(self, NAME = "none"):
        self.name = NAME

class card: # Card will only run if we define the Typing and Ability variable types first
    def __init__(self, NAME = "Untitled", HEALTH = 0, ATTACK = 0, TYPING = Typing(), ABILITY = Ability()):
        self.name = NAME
        self.hp = HEALTH
        self.atk = ATTACK
        self.typing = TYPING # type already exists as a function
        self.ability = ABILITY
    # Hypothetically, we could insert a workaround here to avoid typing self.var infront of every variable.
    def Print(self):
        print("NAME: ", self.name, "\nHP: ", self.hp, "\nATK: ", self.atk, "\nTYPE: ", self.typing.name, "\nABILITY: ", self.ability.name)




import pygame
import random
free_card = card("Free Card", 1, 1, Typing("attack"))