import pygame
import sys
from enemy import EnemyClass
from player import PlayerClass

pygame.init()

screen_width = 800
screen_height = 600
player_mover = [0, 0]

background_colour = [100, 100, 100]

screen = pygame.display.set_mode((screen_width, screen_height))

game_over = False

clock = pygame.time.Clock()

EnemyClass.SetScreenWidthForEnemy(screen_width)

while not game_over:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_mover[0]
            y = player_mover[1]
            if event.key == pygame.K_LEFT:
                PlayerClass.MovePlayerLeft(x, y)
            elif event.key == pygame.K_RIGHT:
                PlayerClass.MovePlayerRight(x, y)

    screen.fill((background_colour))

    PlayerClass.PlayerRender(screen, screen_height, screen_width)
    EnemyClass.EnemyRender(screen, screen_height, screen_width)

    clock.tick(30)

    pygame.display.update()
