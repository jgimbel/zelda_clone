__author__ = 'joel'
from Enemy import enemy
from Sprites.spritesheet import SpriteSheet

class scientist(enemy):
    speed = 50
    def __init__(self, x, y):
        super(scientist, self).__init__(SpriteSheet('Sprites/Enemies/evil_scientist.png'), x, y)
