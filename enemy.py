import pygame
import random
import sys

enemy_size = 30
game_screen_width_for_enemy = 0
enemy_pos = [0, 0]
enemy_colour = (150, 252, 75) #Going for a lime green here

class EnemyClass:
    def SetScreenWidthForEnemy(game_screen_width):
        game_screen_width_for_enemy = game_screen_width
        global enemy_pos
        enemy_pos = [random.randint(0, game_screen_width_for_enemy), 0]
    
    def EnemyRender(game_screen):
        pygame.draw.rect(game_screen, enemy_colour, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

