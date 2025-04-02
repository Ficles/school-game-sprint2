import pygame
import math
from enemies import *
from player import *
from screen import *

pygame.init()
clock = pygame.time.Clock()
screen = Screen()
running = True

screen.load_sprite("player_default", "assets/player/default.bmp")

def get_direction_to_pointer(pos):
    pointer_pos = pygame.mouse.get_pos()
    print(pointer_pos)
    adjacent = pos[1] - pointer_pos[1] 
    opposite = pos[0] - pointer_pos[0]
    angle = math.atan2(opposite, adjacent)
    print(math.degrees(angle))
    return math.degrees(angle)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.draw_sprite("player_default", (200, 200), get_direction_to_pointer((200, 200)))
    screen.update()

    clock.tick(60)

pygame.quit()