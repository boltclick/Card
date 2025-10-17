import pygame
import random as rnd
import array as arr
from Card import *
from Player import *
pygame.init()

player = Player(30, 3)
enemy = Player(30, 3)

screen = pygame.display.set_mode((1920, 1080))
text_font = pygame.font.SysFont("Arial", 30)
def font(name, size):
    return pygame.font.SysFont(name, size)

def draw_text(text, font, color, x, y):
    img = font.render(str(text), True, color)
    screen.blit(img, (x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                break

    screen.fill((0, 0, 0))  # clear the frame

    # Draw cards
    pygame.draw.rect(screen, (255,255,255), (500,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (750,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (1000,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,255,255), (1250,575,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (500,250,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (750,250,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (1000,250,150,225), 1, 12)
    pygame.draw.rect(screen, (255,0,0), (1250,250,150,225), 1, 12)

    pygame.draw.line(screen, (0,192,255), (0,525), (1920,525), 1)

    draw_text("Health = " + str(player.get_health()), font("Arial", 30), (0,255,0), 225, 550)
    draw_text("Health = " + str(enemy.get_health()), font("Arial", 30), (0,255,0), 225, 125)
    draw_text("Energy = " + str(player.get_tenergy()), font("Arial", 30), (64, 128, 255), 1575, 550)
    draw_text("Energy = " + str(enemy.get_tenergy()), font("Arial", 30), (64, 128, 255), 1575, 125)

    if player.health <= 0:
        draw_text("YOU DIE", font("Arial", 300), (0, 255, 0), 250, 500)
    elif enemy.health <= 0:
        draw_text("YOU WIN", font("Arial", 300), (0, 255, 0), 500, 500)


    pygame.display.flip()
pygame.quit()

# from pygame.locals import *
#
# flags = FULLSCREEN | DOUBLEBUF
# screen = pygame.display.set_mode(resolution, flags, 16)