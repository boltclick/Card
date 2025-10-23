import pygame
from Globals import *
pygame.init()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, card, x = 0, y = 0, width = 150, height = 225):
        super().__init__()
        # Load and scale image
        image = card.get_image()
        self.card = card
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.original_image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (width, height))
        # Get rect and set position
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def show(self, x = None, y = None, width = None, height = None):
        x = self.x if x is None else x
        y = self.y if y is None else y
        width = self.width if width is None else width
        height = self.height if height is None else height
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        text_font = font("Arial", 30, True)
        screen.blit(self.image, self.rect)
        if self.card.get_typing() != "passive":
            draw_text(self.card.get_hp(), text_font, red, x+38, y)
            draw_text(self.card.get_atk(), text_font, white, x+100, y)
            draw_text(self.card.get_energy(), text_font, (255, 188, 5), x + 125, y+30)

    def get_rect(self):
        return self.rect

    def get_card(self):
        return self.card

    def rotate_90(self, number_of_rotations = 1):
        if number_of_rotations % 2 != 0:
            temp = self.width
            self.width = self.height
            self.height = temp
        for i in range(number_of_rotations):
            self.image = pygame.transform.rotate(self.image, 90)
        self.show()