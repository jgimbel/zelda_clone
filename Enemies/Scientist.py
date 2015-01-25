__author__ = 'joel'
from random import randrange

from Enemy import enemy
from Sprites.spritesheet import SpriteSheet
from resources import *


class scientist(enemy):
    speed = 50
    def __init__(self, x, y):
        super(scientist, self).__init__(SpriteSheet('Sprites/Enemies/evil_scientist.png'), x, y)

    def kill(self, player):
        super(scientist, self).kill(player)
        for i in range(randrange(1, player.level)):
            scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))
