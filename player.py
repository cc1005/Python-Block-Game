import pygame
import sys

player_colour = (200, 200, 252)
player_size = 30
movement_speed = 15

class PlayerClass:

    def PlayerRender(screen, screen_height, screen_width):
        global player_pos 
        player_pos = [(screen_width/2), screen_height/2 + (screen_height/5 * 2)]
        pygame.draw.rect(screen, player_colour, (player_pos[0], player_pos[1], player_size, player_size))

    def MovePlayerLeft(x, y):
        x -= movement_speed
        player_pos = [x, y]
    
    def MovePlayerRight(x, y):
        x += movement_speed
        player_pos = [x, y]
