import pygame
import sys

enemy_size = 30
enemy_pos = [100, 0]
enemy_colour = (150, 252, 75)

class EnemyClass:
    def EnemyRender(gameScreen):
        pygame.draw.rect(gameScreen, enemy_colour, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))