import pygame
import math
from enemies import *
from player import *
from screen import *

pygame.init()
clock = pygame.time.Clock()
screen = Screen()
player = Player()
bullets = []
running = True

screen.load_sprite("player_default", "assets/player/default.bmp")
screen.load_sprite("player_bullet", "assets/player/bullet.bmp")

while running:
    player.point()
    if player.fire_cooldown > 0: player.fire_cooldown -= 1

    for bullet in bullets:
        bullet.move()
        print((bullet.x, bullet.y))
        screen.draw_sprite("player_bullet", (bullet.x, bullet.y), bullet.direction)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.move(0, player.speed * -1)
    if keys[pygame.K_s]:
        player.move(0, player.speed)
    if keys[pygame.K_a]:
        player.move(player.speed * -1, 0)
    if keys[pygame.K_d]:
        player.move(player.speed, 0)
    if pygame.mouse.get_pressed()[0]:
        if player.fire_cooldown == 0:
            bullets.append(player.shoot())

    screen.draw_sprite(player.sprite, (player.x, player.y), player.direction)
    screen.update()

    clock.tick(60)

pygame.quit()