__author__ = 'joel'
from resources import *
from Items import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.image = pygame.image.load('player.png').convert_alpha()
        self.Pos = [0, 0]
        self.inventory = {
            DIRT: 0,
            GRASS: 0,
            WATER: 0,
            COAL: 0,
            SWORD: sword(),
            SHIELD: False,
            BOW: False
        }
