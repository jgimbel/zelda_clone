__author__ = 'joel'
from pygame.locals import *

from Enemies import *
from resources import *
from Map import *
from link import Player


pygame.init()
SCREEN = pygame.display.set_mode((CAMWIDTH * TILESIZE, CAMHEIGHT * TILESIZE + 50))
pygame.display.set_caption("Zelda Clone")
fpsClock = pygame.time.Clock()
PLAYER = Player()
CAM = Camera(PLAYER, Rect((0,0), (MAPWIDTH, MAPHEIGHT)), SCREEN.subsurface((0, 40, SCREEN.get_width(), SCREEN.get_height() - 40)).get_size())
MAP = Map(PLAYER)
scientist(0, 0)

def draw():
    #CLEAR AND REDRAW SCREEN
    CAM.draw_background(SCREEN, MAP)
    CAM.drawPlayer(SCREEN, PLAYER)
    CAM.drawEnemies(SCREEN, ENEMIES)

while True:

    #UPDATE ALL THE THINGS!!
    dt = fpsClock.tick(24)
    pygame.display.update()
    PLAYER.update(dt, MAP.tilemap)

    ENEMIES.update(PLAYER, dt, PLAYER.arrows, MAP.tilemap)
    CAM.update(PLAYER.rect)

    # GET ALL THE EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    draw()
