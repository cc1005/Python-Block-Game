import pygame
import sys

player_colour = (200, 200, 252)
player_size = 30
movement_speed = 15
player_pos = [0, 0]

class PlayerClass:
    
    def PlayerFirstPosition(screen_height, screen_width):
        global player_pos
        player_pos = [(screen_width/2), screen_height/2 + (screen_height/5 * 2)]

    def ReturnPlayerPos():
        return player_pos

    def PlayerRender(screen):
        pygame.draw.rect(screen, player_colour, (player_pos[0], player_pos[1], player_size, player_size))

    def MovePlayerLeft(x):
        x -= movement_speed
        global player_pos
        player_pos[0] += x
    
    def MovePlayerRight(x):
        x += movement_speed
        global player_pos
        player_pos[0] += x
