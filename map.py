__author__ = 'joel'
import random

from resources import *

TILESIZE = 32
MAPWIDTH = 10
MAPHEIGHT = 10
textures = {
    DIRT: pygame.image.load('4_earthTiles/38earth8.bmp'),
    GRASS: pygame.image.load('1_grassTiles/1grass1.bmp'),
    WATER: pygame.image.load('2_waterTiles/13water3.bmp'),
    COAL: pygame.image.load('4_earthTiles/32earth2.bmp')
}
class Map:
    resources = [DIRT, GRASS, WATER, COAL]
    tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
    def __init__(self, player):
        self.player = player
        for rw in range(MAPHEIGHT):
            for cl in range(MAPWIDTH):
                randomNumber = random.randint(0, 15)
                if randomNumber == 0:
                    tile = COAL
                elif randomNumber == 1 or randomNumber == 2:
                    tile = WATER
                elif 3 <= randomNumber <= 7:
                    tile = GRASS
                else:
                    tile = DIRT

                self.tilemap[rw][cl] = tile

    def placeBlock(self, block):
        if self.player.inventory[block] > 0:
            tile = self.tilemap[self.player.Pos[0]][self.player.Pos[1]]
            self.player.inventory[block] -= 1
            self.tilemap[self.player.Pos[1]][self.player.Pos[0]] = block
            self.player.inventory[tile] += 1