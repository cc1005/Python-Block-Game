import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
player_colour = (150, 150, 252)

screen = pygame.display.set_mode((screen_width, screen_height))

game_over = False

while not game_over:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.draw.rect(screen, player_colour, (400, 300, 50, 50))

    pygame.display.update()