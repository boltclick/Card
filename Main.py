import pygame
from Globals import *
import random as rnd
import array as arr
from Card import *
from Player import *
from Deck import *
from Button import *
from Playerfield import *
from Hand import *
from Sprites import *
from Mouse import *


player = Player(30, 3)
enemy = Player(30, 3)
player_field = Playerfield(575)

# enemy_field = Playerfield(250)
# enemy_field.place_card(A1, 3)
# enemy_field.place_card(S8, 2)
# enemy_field.place_card(A4, 4)
# enemy_field.place_card(S3, 5)

text_font = pygame.font.SysFont("Arial", 30)

while running:
    screen.fill((0,0,0)) # Resets each frame
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(1, 19):
        pygame.draw.line(screen, (30, 30, 30), (i*100, 0), (i*100, 1080), 1)
        for i in range (1, 10):
            pygame.draw.line(screen, (30, 30, 30), (0, i*100), (1920, i*100), 1)

    end_img = pygame.image.load('assets/End_turn.png')
    end_turn = Button(end_img, "End Turn")
    end_turn.show(885, 120, 150, 75, pos)

    deck = Button(pygame.image.load("assets/Deck.png"), "Deck")
    deck.show( 1500, 700, 150, 225, pos)
    player_hand.display()
    # player_hand.display()
    # pygame.time.wait(500)

    # mouse
    pos = pygame.mouse.get_pos()
    place_card_on_field(player_field, player_hand, pos)

    draw_text("Health = " + str(player.get_health()), font("Arial", 30), (0,255,0), 225, 550)
    draw_text("Health = " + str(enemy.get_health()), font("Arial", 30), (0,255,0), 225, 125)
    draw_text("Energy = " + str(player.get_tenergy()), font("Arial", 30), (64, 128, 255), 1575, 550)
    draw_text("Energy = " + str(enemy.get_tenergy()), font("Arial", 30), (64, 128, 255), 1575, 125)

    # Win Condition
    if player.health <= 0:
        draw_text("YOU DIE", font("Arial", 300), (0, 255, 0), 250, 500)
    elif enemy.health <= 0:
        draw_text("YOU WIN", font("Arial", 300), (0, 255, 0), 500, 500)


    # Player Board
    pygame.draw.rect(screen, (255,255,255), (500,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (750,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (1000,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (1250,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (225,600,225,150), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (225,775,225,150), 1, 12)

    # Enemy Board
    pygame.draw.rect(screen, (255,0,0), (500,250,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (750,250,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (1000,250,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (1250,250,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (225,175,225,150), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (225,350,225,150), 1, 12)

    #Line
    pygame.draw.line(screen, (0,192,255), (0,525), (1920,525), 1)
    # pygame.draw.rect(screen, (235,192,255), (1500, 700, 150, 225), 0, 12)




    pygame.display.flip()
pygame.quit()

# from pygame.locals import *
#
# flags = FULLSCREEN | DOUBLEBUF
# screen = pygame.display.set_mode(resolution, flags, 16)