import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT ))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

pygame.quit()