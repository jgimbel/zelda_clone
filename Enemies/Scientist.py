__author__ = 'joel'
from random import randrange

from Enemy import enemy
from Sprites.spritesheet import SpriteSheet


class scientist(enemy):
    def __init__(self, x, y):
        super(scientist, self).__init__(SpriteSheet('Sprites/Enemies/evil_scientist.png'), x, y)
        self.speed = randrange(25, 75)

    def kill(self, player):
        super(scientist, self).kill(player)