__author__ = 'joel'
import random

from resources import *
from Tile import tile

class Map:
    tilemap = pygame.sprite.Group()
    def __init__(self, player):
        self.player = player
        back = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
        for rw in range(MAPHEIGHT):
            for cl in range(MAPWIDTH):
                randomNumber = random.randint(0, 15)
                if randomNumber == 0:
                    t = COAL
                    tile.blocked = True
                elif randomNumber == 1 or randomNumber == 2:
                    t = WATER
                elif 3 <= randomNumber <= 7:
                    t = GRASS
                else:
                    t = DIRT

                self.tilemap.add(tile(t, [cl * TILESIZE, rw * TILESIZE]))

    def draw(self, SCREEN, x, y):
        self.tilemap.update(x, y)
        self.tilemap.draw(SCREEN)