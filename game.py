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
        self.CAM = Camera(self.SCREEN, Rect((0,0), (MAPWIDTH, MAPHEIGHT)), self.SCREEN.subsurface((0, 40, self.SCREEN.get_width(), self.SCREEN.get_height() - 40)).get_size(), h ,w)
        self.MAP = Map(self.PLAYER)
        self.SCREEN = self.CAM.toggle_fullscreen()
        self.paused = True
        self.inventory = False
        self.betweenWave = False
        self.wave = 1
        self.waveCounter = 0
        self.menu = [Option("NEW GAME", ((w/2) -20, (h/3)), self.newGame), Option("QUIT GAME", ((w/2) -20, (4 * h/9)), self.quit),
                     Option("Resume", ((w/2) -15, ( 5 * h/9)), self.togglePause)]

        pygame.display.set_caption("Zelda Clone")

        pygame.mixer.music.load('Sounds/Music/TheLoomingBattle_0.OGG')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()
        scientist(0,0)
        while True:
            self.update()

    def newGame(self):
        self.PLAYER = Player()
        ENEMIES.remove(ENEMIES.sprites())
        self.paused = False
        self.wave = 1
        self.nextWave()

    def quit(self):
        pygame.quit()
        sys.exit()

    def togglePause(self):
        if self.paused:
            self.paused = False
        else:
            self.paused = True

    def nextWave(self):
        #TODO epic monsters on % 5 levels,
        #TODO super monsters on % 10 levels (still gets other bosses from % 5),
        for i in range(self.wave * 5):
            scientist(randrange(0, MAPWIDTH * TILESIZE), randrange(0, MAPHEIGHT * TILESIZE))

    def draw(self):
        #CLEAR AND REDRAW SCREEN
        self.CAM.draw_background(self.MAP)
        self.CAM.drawPlayer(self.PLAYER)
        self.CAM.drawEnemies(ENEMIES)
        self.CAM.drawHUD(self.PLAYER, self.wave)
        self.CAM.drawItems(ITEMS)

        if self.inventory:
            self.CAM.drawInventory(self.PLAYER.inventory)
        if self.paused:
            self.CAM.drawMenu(self.menu)

        if self.betweenWave:
            self.CAM.drawTimer(self.waveCounter)

    def update(self):

        dt = self.fpsClock.tick(60)
        if not self.paused:
            if not self.betweenWave and len(ENEMIES) <= 0:
                self.wave += 1
                self.betweenWave = True

            if self.betweenWave:
                if self.waveCounter > 10000:
                    self.betweenWave = False
                    self.waveCounter = 0
                    self.nextWave()
                else:
                    self.waveCounter += dt

            #UPDATE ALL THE THINGS!!
            self.alive = self.PLAYER.update(dt, self.MAP.tilemap)
            ENEMIES.update(self.PLAYER, dt, self.MAP.tilemap)
            self.CAM.update(self.PLAYER.rect)

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
                if event.key == K_TAB:
                    if self.inventory:
                        self.inventory = False
                    else:
                        self.inventory = True
                if event.key == K_ESCAPE:
                    self.togglePause()
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