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
class Map:
    resources = [DIRT, GRASS, WATER, COAL]
    tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]
    def __init__():
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

                tilemap[rw][cl] = tile



    def placeBlock(block):
        if PLAYER.inventory[block] > 0:
            tile = tilemap[PLAYER.Pos[0]][PLAYER.Pos[1]]
            PLAYER.inventory[block] -= 1
            tilemap[PLAYER.Pos[1]][PLAYER.Pos[0]] = block
            PLAYER.inventory[tile] += 1