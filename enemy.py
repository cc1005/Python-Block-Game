import pygame
import random
import sys

enemy_size = 30
enemy_colour = (150, 252, 75) #Going for a lime green here
enemy_speed = 10

class EnemyClass:
    def SetScreenWidthForEnemy(game_screen_width):
        global enemy_pos
        enemy_pos = [random.randint(0, game_screen_width - enemy_size), 0]
        return enemy_pos
    
    def EnemyRender(game_screen, game_screen_height, game_screen_width):
        if enemy_pos[1] >= 0 and enemy_pos[1] < game_screen_height:
            enemy_pos[1] += enemy_speed
        else:
            enemy_pos[0] = random.randint(0, game_screen_width - enemy_size)
            enemy_pos[1] = 0
        pygame.draw.rect(game_screen, enemy_colour, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

