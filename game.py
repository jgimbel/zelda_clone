__author__ = 'joel'
from pygame.locals import *
import pygame

from Map import *
from link import Player


pygame.init()
SCREEN = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + 50))
pygame.display.set_caption("Zelda Clone")
fpsClock = pygame.time.Clock()
PLAYER = Player()
MAP = Map(PLAYER)

while True:

    #UPDATE ALL THE THINGS!!
    dt = fpsClock.tick(24)
    pygame.display.update()
    PLAYER.update(dt)

    # GET ALL THE EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #CLEAR AND REDRAW SCREEN
    SCREEN.fill(BLACK)
    MAP.draw(SCREEN)
    PLAYER.draw(SCREEN)
