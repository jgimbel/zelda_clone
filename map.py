__author__ = 'joel'
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

resources = [DIRT, GRASS, WATER, COAL]
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
