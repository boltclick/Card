import pygame
import time
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
running = True
last_clicked = 0
pos = pygame.mouse.get_pos()

# def delete(x,y):
#     delete = pygame.draw.rect(screen, (0, 0, 0), (x, y, 150, 225), 0, 12)

def clicked():
    global last_clicked
    if pygame.mouse.get_pressed()[0] == 1 and (last_clicked < pygame.time.get_ticks() - 500):
        last_clicked = pygame.time.get_ticks()
        return True
    return False

def font(name, size):
    return pygame.font.SysFont(name, size)

def draw_text(text, font, color, x, y):
    img = font.render(str(text), True, color)
    screen.blit(img, (x, y))