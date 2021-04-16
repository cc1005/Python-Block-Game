import pygame
import sys
from enemy import EnemyClass
from player import PlayerClass

pygame.init()

screen_width = 800
screen_height = 600
player_mover = [0, 0]
k_left_is_pressed = False
k_right_is_pressed = False

background_colour = [100, 100, 100]

screen = pygame.display.set_mode((screen_width, screen_height))

game_over = False

clock = pygame.time.Clock()

EnemyClass.SetScreenWidthForEnemy(screen_width)
PlayerClass.PlayerFirstPosition(screen_height, screen_width)

while not game_over:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_mover[0]
            if event.key == pygame.K_LEFT:
                k_left_is_pressed = True
            elif event.key == pygame.K_RIGHT:
                k_right_is_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                k_left_is_pressed = False
            elif event.key == pygame.K_RIGHT:
                k_right_is_pressed = False

        if k_left_is_pressed:
            PlayerClass.MovePlayerLeft(x)

        if k_right_is_pressed:
            PlayerClass.MovePlayerRight(x)

    screen.fill((background_colour))

    PlayerClass.PlayerRender(screen)
    EnemyClass.EnemyRender(screen, screen_height, screen_width)

    clock.tick(30)

    pygame.display.update()
