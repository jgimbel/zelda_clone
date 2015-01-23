__author__ = 'joel'
import math

from pygame.locals import *

from resources import *
from Items import *


DIAG = 1 / math.sqrt(2)

class Player(pygame.sprite.Sprite):
    speed = 150
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.image = pygame.image.load('player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        self.vx = 0
        self.vy = 0
        self.inventory = {
            DIRT: 0,
            GRASS: 0,
            WATER: 0,
            COAL: 0,
            SWORD: sword(),
            SHIELD: shield(),
            BOW: False
        }

    def update(self, dt):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.vy = -self.speed
        if keys[K_DOWN]:
            self.vy =  self.speed
        if keys[K_LEFT]:
            self.vx = -self.speed
        if keys[K_RIGHT]:
            self.vx =  self.speed

        if self.vx and self.vy:
            self.vx *= DIAG
            self.vy *= DIAG

        dt = dt / 1000.0
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt