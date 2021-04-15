import pygame
import sys
from enemy import EnemyClass

pygame.init()

screen_width = 800
screen_height = 600

player_colour = (150, 150, 252)
player_size = 30
player_pos = [(screen_width/2), screen_height/2 + (screen_height/5 * 2)]
background_colour = [252, 252, 252]

screen = pygame.display.set_mode((screen_width, screen_height))

game_over = False

while not game_over:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.KEYDOWN:
        x = player_pos[0]
        y = player_pos[1]
        movement_speed = 0.5
        if event.key == pygame.K_LEFT:
            x -= movement_speed
        elif event.key == pygame.K_RIGHT:
            x += movement_speed

        player_pos = [x, y]

    screen.fill((background_colour))

    pygame.draw.circle(screen, player_colour, (player_pos[0], player_pos[1]), player_size)
    EnemyClass.EnemyRender(screen)
    pygame.display.update()