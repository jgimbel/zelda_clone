__author__ = 'joel'
from pygame.locals import *

from Items import *

from map import *
from link import Player


pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
pygame.display.set_caption("Minecraft")

PLAYER = Player()
MAP = Map(PLAYER)

while True:

    # GET ALL THE EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_RIGHT) and PLAYER.Pos[0] < MAPWIDTH - 1:
                PLAYER.Pos[0] += 1

            if (event.key == K_LEFT) and PLAYER.Pos[0] > 0:
                PLAYER.Pos[0] -= 1

            if (event.key == K_UP) and PLAYER.Pos[1] > 0:
                PLAYER.Pos[1] -= 1

            if (event.key == K_DOWN) and PLAYER.Pos[1] < MAPHEIGHT - 1:
                PLAYER.Pos[1] += 1

            if event.key == K_SPACE:
                tile = MAP.tilemap[PLAYER.Pos[1]][PLAYER.Pos[0]]
                PLAYER.inventory[tile] += 1
                MAP.tilemap[PLAYER.Pos[1]][PLAYER.Pos[0]] = DIRT

            if event.key == K_1:
                MAP.placeBlock(DIRT)

            if event.key == K_2:
                MAP.placeBlock(GRASS)

            if event.key == K_3:
                MAP.placeBlock(WATER)

            if event.key == K_4:
                MAP.placeBlock(COAL)

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[MAP.tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

    DISPLAYSURF.blit(PLAYER.image, (PLAYER.Pos[0] * TILESIZE, PLAYER.Pos[1] * TILESIZE))
    if type(PLAYER.inventory[SWORD]) == sword:
        DISPLAYSURF.blit(PLAYER.inventory[SWORD].image, (PLAYER.Pos[0] * TILESIZE + 0, PLAYER.Pos[1] * TILESIZE + 10))

    if type(PLAYER.inventory[SHIELD]) == shield:
        DISPLAYSURF.blit(PLAYER.inventory[SHIELD].image, (PLAYER.Pos[0] * TILESIZE + 10, PLAYER.Pos[1] * TILESIZE + 14))

    placePosition = 10
    for item in MAP.resources:
        DISPLAYSURF.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 30
        textObj = INVFONT.render(str(PLAYER.inventory[item]), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 50

    pygame.display.update()
    fpsClock.tick(24)