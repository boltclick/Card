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


player_field = Playerfield(575)
player_hand.add_card(free_card)
i = 0 # We can't use a for loop, because if you have for i in range(0,2), and do i -= 1,
while i < 2: # it doesn't lower i's index, which is what matters, since range is a tuple/list
    rand = rnd.randint(0, len(deck) - 1)
    if deck[rand] not in player_hand.get_cards():
        player_hand.add_card(deck[rand])
        i += 1

# enemy_field = Playerfield(250, -100)
# #enemy cards
# enemy_field.place_card(EP1, 0)
# enemy_field.place_card(EP2, 1)
# enemy_field.place_card(ES4, 2)
# enemy_field.place_card(EA2, 3)
# enemy_field.place_card(Catastrophevil, 4)
# enemy_field.place_card(ES5, 5)
Turn = 0



text_font = pygame.font.SysFont("Arial", 30)

while running:
    # Board Setup
    if True:
        screen.fill((0,0,0)) # Resets each frame
        # Grid Lines
        for i in range(1, 19):
            pygame.draw.line(screen, (30, 30, 30), (i * 100, 0), (i * 100, 1080), 1)
        for i in range(1, 10):
            pygame.draw.line(screen, (30, 30, 30), (0, i * 100), (1920, i * 100), 1)
        # Player Board
        pygame.draw.rect(screen, (255,255,255), (500,575,150,225), 1, 12)
        draw_text("S", font("Arial", 200), (255, 255, 255), 520, 565)
        pygame.draw.rect(screen, (255,255,255), (750,575,150,225), 1, 12)
        draw_text("A", font("Arial", 200), (255, 255, 255), 770, 565)
        pygame.draw.rect(screen, (255,255,255), (1000,575,150,225), 1, 12)
        draw_text("A", font("Arial", 200), (255, 255, 255), 1020, 565)
        pygame.draw.rect(screen, (255,255,255), (1250,575,150,225), 1, 12)
        draw_text("S", font("Arial", 200), (255, 255, 255), 1270, 565)
        pygame.draw.rect(screen, (255,255,255), (225,600,225,150), 1, 12)
        draw_text("P", font("Arial", 125), (255, 255, 255), 310, 600)
        pygame.draw.rect(screen, (255,255,255), (225,775,225,150), 1, 12)
        draw_text("P", font("Arial", 125), (255, 255, 255), 310, 775)

        # Enemy Board
        pygame.draw.rect(screen, (255,0,0), (500,250,150,225), 1, 12)
        draw_text("S", font("Arial", 200), (255, 0, 0), 520, 250)
        draw_text("A", font("Arial", 200), (255, 0, 0), 770, 250)
        draw_text("A", font("Arial", 200), (255, 0, 0), 1020, 250)
        draw_text("S", font("Arial", 200), (255, 0, 0), 1270, 250)
        draw_text("P", font("Arial", 125), (255, 0, 0), 310, 175)
        draw_text("P", font("Arial", 125), (255, 0, 0), 310, 350)
        pygame.draw.rect(screen, (255,0,0), (750,250,150,225), 1, 12)
        pygame.draw.rect(screen, (255,0,0), (1000,250,150,225), 1, 12)
        pygame.draw.rect(screen, (255,0,0), (1250,250,150,225), 1, 12)
        pygame.draw.rect(screen, (255,0,0), (225,175,225,150), 1, 12)
        pygame.draw.rect(screen, (255,0,0), (225,350,225,150), 1, 12) #
    pos = pygame.mouse.get_pos()
    clicked = is_clicked() # is_clicked = is_clicked() will not work, because they have the same name
    # print(clicked)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    enemy_field.show_field()
    if clicked:
        print(player_field.get_field())

    end_img = pygame.image.load('assets/End_turn.png')
    end_turn = Button(end_img, "End Turn", Turn)
    end_turn.show(885, 120, 150, 75, pos, clicked, player_hand, player_field, enemy_field)

    deck = Button(pygame.image.load("assets/Deck.png"), "Deck", Turn)
    deck.show(1500, 700, 150, 225, pos, clicked, player_hand, player_field)
    player_hand.display(clicked)
    # player_hand.display()
    # pygame.time.wait(500)

    # mouse
    place_card_on_field(player_field, player_hand, pos, clicked)
    player_field.show_field()
    if clicked:
        print(player_field.get_field())

    draw_text("Health = " + str(player.get_health()), font("Arial", 30), (0,255,0), 225, 550)
    draw_text("Health = " + str(enemy.get_health()), font("Arial", 30), (0,255,0), 225, 125)
    draw_text("Energy = " + str(player.get_tenergy()), font("Arial", 30), (64, 128, 255), 1575, 550)
    draw_text("Energy = " + str(enemy.get_tenergy()), font("Arial", 30), (64, 128, 255), 1575, 125)

    pygame.draw.line(screen, (0,192,255), (0,525), (1920,525), 1)
    # Win Condition
    if player.health <= 0:
        screen.fill((20,0,0))
        draw_text("YOU DIED", font("Arial", 300), (255, 0, 0), 375, 400)
    elif enemy.health <= 0:
        screen.fill((0, 128, 0))
        draw_text("YOU WIN", font("Arial", 300), (64, 255, 64), 450, 400)

    #Line
    # pygame.draw.rect(screen, (235,192,255), (1500, 700, 150, 225), 0, 12)




    pygame.display.flip()
pygame.quit()

# from pygame.locals import *
#
# flags = FULLSCREEN | DOUBLEBUF
# screen = pygame.display.set_mode(resolution, flags, 16)