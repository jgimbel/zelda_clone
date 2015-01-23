__author__ = 'joel'
import random
from pygame.locals import *
from map import *
from link import Player
from Items import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 1000))
pygame.display.set_caption("Minecraft")

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

PLAYER = Player()


def placeBlock(block):
    if PLAYER.inventory[block] > 0:
        tile = tilemap[PLAYER.Pos[0]][PLAYER.Pos[1]]
        PLAYER.inventory[block] -= 1
        tilemap[PLAYER.Pos[1]][PLAYER.Pos[0]] = block
        PLAYER.inventory[tile] += 1


fpsClock = pygame.time.Clock()

while True:

    # GET ALL THE EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and PLAYER.Pos[0] < (MAPWIDTH) - 1:
                PLAYER.Pos[0] += 1

            if (event.key == K_LEFT) and PLAYER.Pos[0] > 0:
                PLAYER.Pos[0] -= 1

            if (event.key == K_UP) and PLAYER.Pos[1] > 0:
                PLAYER.Pos[1] -= 1

            if (event.key == K_DOWN) and PLAYER.Pos[1] < (MAPHEIGHT) - 1:
                PLAYER.Pos[1] += 1

            if event.key == K_SPACE:
                tile = tilemap[PLAYER.Pos[1]][PLAYER.Pos[0]]
                PLAYER.inventory[tile] += 1
                tilemap[PLAYER.Pos[1]][PLAYER.Pos[0]] = DIRT

            if event.key == K_1:
                placeBlock(DIRT)

            if event.key == K_2:
                placeBlock(GRASS)

            if event.key == K_3:
                placeBlock(WATER)

            if event.key == K_4:
                placeBlock(COAL)

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

    DISPLAYSURF.blit(PLAYER.image, (PLAYER.Pos[0] * TILESIZE, PLAYER.Pos[1] * TILESIZE))

    placePosition = 10
    for item in resources:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 30
        textObj = INVFONT.render(str(PLAYER.inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 50

    pygame.display.update()
    fpsClock.tick(24)