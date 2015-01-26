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
        self.VOLUME = 1.0
        self.MUSIC_PAUSE = True
        self.alive = True
        self.SCREEN = pygame.display.set_mode((CAMWIDTH * TILESIZE, CAMHEIGHT * TILESIZE + 50))
        self.fpsClock = pygame.time.Clock()
        self.PLAYER = Player()
        self.CAM = Camera(self.PLAYER, Rect((0,0), (MAPWIDTH, MAPHEIGHT)), self.SCREEN.subsurface((0, 40, self.SCREEN.get_width(), self.SCREEN.get_height() - 40)).get_size(), h ,w)
        self.MAP = Map(self.PLAYER)
        self.SCREEN = self.CAM.toggle_fullscreen()
        self.paused = True
        #TODO: give the option a function to call when clicked
        self.menu = [Option("NEW GAME", ((w/2) -20, (h/3)), self.newGame), Option("QUIT GAME", ((w/2) -20, (4 * h/9)), self.quit),
                     Option("OPTIONS", ((w/2) -15, ( 5 * h/9)), self.newGame)]

        pygame.display.set_caption("Zelda Clone")

        pygame.mixer.music.load('Sounds/Music/TheLoomingBattle_0.OGG')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()
        while True:
            self.update()

    def newGame(self):
        self.PLAYER = Player()
        ENEMIES = pygame.sprite.Group()
        scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))
        self.paused = False

    def quit(self):
        pygame.quit()
        sys.exit()

    def drawMenu(self):
        w = pygame.display.Info().current_w
        h = pygame.display.Info().current_h
        m = pygame.Surface(( w/ 2, h / 2))
        m.fill(BLACK)
        self.SCREEN.blit(m, [w - (w * 3/4), h - (h * 3/4)])

        for option in self.menu:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw(self.SCREEN)


    def draw(self):
        #CLEAR AND REDRAW SCREEN
        self.CAM.draw_background(self.SCREEN, self.MAP)
        self.CAM.drawPlayer(self.SCREEN, self.PLAYER)
        self.CAM.drawEnemies(self.SCREEN, ENEMIES)
        self.CAM.drawHUD(self.PLAYER)
        if self.paused:
            self.drawMenu()


    def update(self):
        dt = self.fpsClock.tick(60)
        if not self.paused:
            #UPDATE ALL THE THINGS!!
            self.alive = self.PLAYER.update(dt, self.MAP.tilemap)
            ENEMIES.update(self.PLAYER, dt, self.PLAYER.arrows, self.MAP.tilemap, self.PLAYER)
            self.CAM.update(self.PLAYER.rect, self.SCREEN)

        if not self.alive:
            self.paused = True

        # GET ALL THE EVENTS
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit()
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
                    self.VOLUME += 0.05
                    if self.VOLUME > 1.0:
                        self.VOLUME = 1.0
                    pygame.mixer.music.set_volume(self.VOLUME)
                if event.key == K_o:
                    self.VOLUME -= 0.05
                    if self.VOLUME < 0.0:
                        self.VOLUME = 0.0
                    pygame.mixer.music.set_volume(self.VOLUME)
        self.draw()
        pygame.display.update()

if __name__ == "__main__":
    Game()