__author__ = 'joel'
from pygame.locals import *

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
               PLAYER.shootArrow()
               PLAYER.inventory[ARROWS] -=1

    #UPDATE ALL THE THINGS!!
    PLAYER.update(24)

    #CLEAR AND REDRAW SCREEN
    SCREEN.fill(BLACK)
    MAP.draw(SCREEN)
    PLAYER.draw(SCREEN)
    PLAYER.arrows.draw(SCREEN)

    placePosition = 10
    for item in MAP.resources:
        SCREEN.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 30
        textObj = INVFONT.render(str(PLAYER.inventory[item]), True, WHITE, BLACK)
        SCREEN.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
        placePosition += 50

    pygame.display.update()
    fpsClock.tick(24)