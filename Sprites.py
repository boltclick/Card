import pygame
from Globals import *
pygame.init()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x = 0, y = 0, width = 150, height = 225):
        super().__init__()
        # Load and scale image
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
        self.rect.center = (x,y)
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect