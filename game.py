__author__ = 'joel'
from random import randrange

from pygame.locals import *

from Enemies import *
from resources import *
from Map import *
from link import Player

class Game():
    def __init__(self):

        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        info = pygame.display.Info()
        w = info.current_w
        h = info.current_h

        self.MUSIC_PAUSE = True
        self.alive = True
        self.SCREEN = pygame.display.set_mode((CAMWIDTH * TILESIZE, CAMHEIGHT * TILESIZE + 50))
        self.fpsClock = pygame.time.Clock()
        self.PLAYER = Player()
        self.CAM = Camera(self.PLAYER, Rect((0,0), (MAPWIDTH, MAPHEIGHT)), self.SCREEN.subsurface((0, 40, self.SCREEN.get_width(), self.SCREEN.get_height() - 40)).get_size(), h ,w)
        self.MAP = Map(self.PLAYER)
        self.SCREEN = self.CAM.toggle_fullscreen()
        self.paused = False
        #TODO: give the option a function to call when clicked
        self.menu = [Option(self.SCREEN, "NEW GAME", (140, 105)), Option(self.SCREEN, "LOAD GAME", (135, 155)),
                     Option(self.SCREEN, "OPTIONS", (145, 205))]

        pygame.display.set_caption("Zelda Clone")
        scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))
        scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))

        pygame.mixer.music.load('Music/HoaF.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()
        while True:
            self.update()

    def drawMenu(self):
        for option in self.menu:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw()

    def draw(self):
        #CLEAR AND REDRAW SCREEN
        self.CAM.draw_background(self.SCREEN, self.MAP)
        self.CAM.drawPlayer(self.SCREEN, self.PLAYER)
        self.CAM.drawEnemies(self.SCREEN, ENEMIES)
        self.CAM.drawHUD(self.PLAYER)
        if self.paused:
            self.drawMenu()
            self.CAM.draw_pause(self.SCREEN)


    def update(self):
        dt = self.fpsClock.tick(60)
        if not self.paused:
            #UPDATE ALL THE THINGS!!
            self.alive = self.PLAYER.update(dt, self.MAP.tilemap)
            ENEMIES.update(self.PLAYER, dt, self.PLAYER.arrows, self.MAP.tilemap, self.PLAYER)
            self.CAM.update(self.PLAYER.rect, self.SCREEN)

        if not self.alive:
            pygame.quit()
            sys.exit()

        # GET ALL THE EVENTS
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.paused and event.button == 1:
                    for option in self.menu:
                        if option.rect.collidepoint(pygame.mouse.get_pos()):
                            option.function()

            if event.type == KEYDOWN:
                if event.key == 102:
                    SCREEN = self.CAM.toggle_fullscreen()
                if event.key == K_ESCAPE:
                    if self.paused:
                        self.paused = False
                    else:
                        self.paused = True
                if event.key == K_BACKSPACE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_m:
                    if self.MUSIC_PAUSE:
                        pygame.mixer.music.unpause()
                        self.MUSIC_PAUSE = False
                    else:
                        pygame.mixer.music.pause()
                        self.MUSIC_PAUSE = True
                if event.key == K_p:
                    VOLUME += 0.05
                    if VOLUME > 1.0:
                        VOLUME = 1.0
                    pygame.mixer.music.set_volume(VOLUME)
                if event.key == K_o:
                    VOLUME -= 0.05
                    if VOLUME < 0.0:
                        VOLUME = 0.0
                    pygame.mixer.music.set_volume(VOLUME)
        self.draw()
        pygame.display.update()

if __name__ == "__main__":
    Game()