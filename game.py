__author__ = 'joel'
from pygame.locals import *

from map import *
from link import Player


pygame.init()
SCREEN = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
pygame.display.set_caption("Zelda Clone")

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

    #UPDATE ALL THE THINGS!!

    #CLEAR AND REDRAW SCREEN
    SCREEN.fill(BLACK)
    MAP.draw(SCREEN)
    PLAYER.draw(SCREEN)

    dt = fpsClock.tick(24)
    pygame.display.update()

    PLAYER.update(dt)