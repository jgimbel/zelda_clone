__author__ = 'joel'
from pygame.locals import *

from Items import *
from map import *
from link import Player


pygame.init()
SCREEN = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
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

            if event.key == K_SPACE:
                if type(PLAYER.inventory[BOW]) == arrow:
                    

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
            SCREEN.blit(textures[MAP.tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

    PLAYER.update(24)

    SCREEN.blit(PLAYER.image, PLAYER.rect)

    if type(PLAYER.inventory[SWORD]) == sword:
        SCREEN.blit(PLAYER.inventory[SWORD].image, (PLAYER.rect.topleft[0], PLAYER.rect.topleft[1] + 10))

    if type(PLAYER.inventory[SHIELD]) == shield:
        SCREEN.blit(PLAYER.inventory[SHIELD].image, (PLAYER.rect[0] + 10, PLAYER.rect[1] + 14))

    placePosition = 10
    for item in MAP.resources:
        SCREEN.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 30
        textObj = INVFONT.render(str(PLAYER.inventory[item]), True, WHITE, BLACK)
        SCREEN.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 50

    pygame.display.update()
    fpsClock.tick(24)