__author__ = 'joel'
import random

from resources import *
from Floor import *

TILESIZE = 32
MAPWIDTH = 10
MAPHEIGHT = 10
class Map:
    resources = [DIRT, GRASS, WATER, COAL]
    tilemap = pygame.sprite.Group()
    def __init__(self, player):
        self.player = player
        back = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
        for rw in range(MAPHEIGHT):
            for cl in range(MAPWIDTH):
                randomNumber = random.randint(0, 15)
                if randomNumber == 0:
                    t = COAL
                elif randomNumber == 1 or randomNumber == 2:
                    t = WATER
                elif 3 <= randomNumber <= 7:
                    t = GRASS
                else:
                    t = DIRT

                self.tilemap.add(tile(t, [cl * TILESIZE, rw * TILESIZE]))

    def placeBlock(self, block):
        if self.player.inventory[block] > 0:
            tile = self.tilemap[self.player.Pos[0]][self.player.Pos[1]]
            self.player.inventory[block] -= 1
            self.tilemap[self.player.Pos[1]][self.player.Pos[0]] = block
            self.player.inventory[tile] += 1

    def draw(self, SCREEN):
        self.tilemap.draw(SCREEN)