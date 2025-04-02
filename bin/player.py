from math import radians, degrees

import pygame
import math


def get_direction_to_pointer(pos):
    pointer_pos = pygame.mouse.get_pos()
    adjacent = pos[1] - pointer_pos[1]
    opposite = pos[0] - pointer_pos[0]
    angle = math.atan2(opposite, adjacent)
    return math.degrees(angle)

def directed_to_global(direction, distance):
    hypotenuse = distance
    opposite = 0
    adjacent = 0
    ratio = math.sin(radians(direction))
    opposite = hypotenuse * ratio
    adjacent = math.sqrt(hypotenuse ** 2 - opposite ** 2)
    if -90 > direction or direction > 90:
        x = opposite * -1
        y = adjacent
    else:
        x = opposite * -1
        y = adjacent * -1

    return x, y
#Bomb
#Bullet
#Player

class Bullet:
    def __init__(self, speed, damage, direction, pos):
        self.speed = speed
        self.damage = damage
        self.direction = direction
        self.x = pos[0]
        self.y = pos[1]

    def move(self):
        x, y = directed_to_global(self.direction, self.speed)
        self.x += x
        self.y += y

class Player:
    def __init__(self):
        self.x = 640
        self.y = 360
        self.direction = 0
        self.sprite = "player_default"
        self.speed = 2
        self.fire_rate = 30
        self.fire_cooldown = 0
        self.damage = 1
        self.bullet_speed = 5
        self.barrel_length = 36

    def point(self):
        self.direction = get_direction_to_pointer((self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def step(self, distance):
        x, y = directed_to_global(self.direction, distance)

        self.move(x, y)

    def shoot(self):
        self.fire_cooldown = self.fire_rate
        spawn_x = self.x
        spawn_y = self.y
        barrel_x, barrel_y = directed_to_global(self.direction, self.barrel_length)
        spawn_x += barrel_x
        spawn_y += barrel_y
        bullet = Bullet(self.bullet_speed, self.damage, self.direction, (spawn_x, spawn_y))
        return bullet
