__author__ = 'joel'
from random import randrange

from Enemy import enemy
from Sprites.spritesheet import SpriteSheet
from resources import *


class scientist(enemy):
    def __init__(self, x, y):
        super(scientist, self).__init__(SpriteSheet('Sprites/Enemies/evil_scientist.png'), x, y)
        self.speed = randrange(25, 75)

    def kill(self, player):
        super(scientist, self).kill(player)
        new_scientist = randrange(0, player.level)
        if new_scientist == 0:
            new_scientist = 1
        for i in range(new_scientist):
            scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))
