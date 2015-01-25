__author__ = 'joel'
from random import randrange

from pygame.locals import *

from Enemies import *
from resources import *
from Map import *
from link import Player

pygame.init()
info = pygame.display.Info()
w = info.current_w
h = info.current_h
SCREEN = pygame.display.set_mode((CAMWIDTH * TILESIZE, CAMHEIGHT * TILESIZE + 50))
pygame.display.set_caption("Zelda Clone")
fpsClock = pygame.time.Clock()
PLAYER = Player()
CAM = Camera(PLAYER, Rect((0,0), (MAPWIDTH, MAPHEIGHT)), SCREEN.subsurface((0, 40, SCREEN.get_width(), SCREEN.get_height() - 40)).get_size(), h ,w)
MAP = Map(PLAYER)
SCREEN = CAM.toggle_fullscreen()
scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))
scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))
scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))
paused = False

def draw():
    #CLEAR AND REDRAW SCREEN
    CAM.draw_background(SCREEN, MAP)
    CAM.drawPlayer(SCREEN, PLAYER)
    CAM.drawEnemies(SCREEN, ENEMIES)
    CAM.drawHUD(PLAYER)

while True:
    dt = fpsClock.tick(24)
    if not paused:
        #UPDATE ALL THE THINGS!!
        pygame.display.update()
        alive = PLAYER.update(dt, MAP.tilemap)
        ENEMIES.update(PLAYER, dt, PLAYER.arrows, MAP.tilemap, PLAYER)
        CAM.update(PLAYER.rect, SCREEN)

    if not alive:
        pygame.quit()
        sys.exit()

    # GET ALL THE EVENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == 102:
                SCREEN = CAM.toggle_fullscreen()
            if event.key == K_ESCAPE:
                if paused:
                    paused = False
                else:
                    paused = True
            if event.key == K_BACKSPACE:
                pygame.quit()
                sys.exit()
    draw()
