__author__ = 'joel'

from pygame.locals import *

from resources import *


class Camera(object):

    def __init__(self,screen, bounds, size, h, w):
        self.bounds = bounds
        self.rect = Rect((0,0), size)
        self.fullscreen = False
        self.FULLH = h
        self.FULLW = w
        self.screen = screen
    def update(self, target):
        self.rect.center = target.center
        self.rect = Rect(self.rect.topleft, self.screen.subsurface((0, 0, self.screen.get_width(), self.screen.get_height())).get_size())
        #self.rect.clamp_ip(self.bounds)

    def draw_background(self, bg):
        self.screen.fill(BLACK)
        bg.draw(self.screen, self.rect)

    def draw_pause(self):
        w,h = self.screen.get_width(), self.screen.get_height()
        text = INVFONT.render("PAUSED", True, WHITE, BLACK)

        hud = text.get_rect()
        hud.topleft = [w/2 - + hud.size[0] / 2, h/2 - 38]
        self.screen.blit(text, hud)


    def rel_rect(self, rect, parent):
        return Rect((rect.x - parent.x, rect.y - parent.y), rect.size)

    def drawPlayer(self, player):
        if self.rect.colliderect(player.rect):
            r = self.rel_rect(player.rect, self.rect)
            player.draw(self.screen, r)

        for a in player.inventory[ARROWS]:
            if self.rect.colliderect(a.rect):
                r = self.rel_rect(a.rect, self.rect)
                a.draw(self.screen, r)

    def drawEnemies(self, enemies):

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                r = self.rel_rect(enemy.rect, self.rect)
                enemy.draw(self.screen, r)

    def drawTimer(self, timer):
        w = self.screen.get_width()
        text = INVFONT.render("Time to next wave: " + str(30 - int(timer/1000)), True, WHITE, BLACK).convert_alpha()

        hud = text.get_rect()
        hud.topleft = [w/2 - hud.size[0]/2, 7]
        self.screen.blit(text, hud)

    def drawItems(self, items):
        for i in items:
            i.draw(self.screen, self.rel_rect(i.rect, self.rect))


    def drawHUD(self, player, wave):
        h =self.screen.get_height()
        text = INVFONT.render("arrows: %s, Enemies: %s, Wave: %s" % (str(player.inventory[QUIVER]), str(len(ENEMIES)), str(wave)), True, WHITE, BLACK).convert_alpha()

        hud = text.get_rect()
        hud.topleft = [0, h - hud.size[1] - 9]
        self.screen.blit(text, hud)

        hearts = pygame.Surface((10 * player.maxhearts, 8))

        for i in range(int(math.ceil(player.maxhearts))):
            hr = HEART.get_rect()
            hr.topleft = [(i*10), 0]
            if i <= player.hearts:
                hearts.blit(HEART, hr)
            else:
                hearts.blit(EMPTY_HEART, hr)
        hr = hearts.get_rect()
        hr.topleft = [0, h - hr.size[1]]
        hearts.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.screen.blit(hearts.convert_alpha(), hr)


    def toggle_fullscreen(self):
        screen = pygame.display.get_surface()
        if self.fullscreen:
            SCREEN = pygame.display.set_mode((CAMWIDTH * TILESIZE, CAMHEIGHT * TILESIZE + 50))
            self.fullscreen = False
        else:
            SCREEN = pygame.display.set_mode((self.FULLW, self.FULLH))
            self.fullscreen = True

        tmp = screen.convert()
        caption = pygame.display.get_caption()

        w,h = screen.get_width(),screen.get_height()
        flags = screen.get_flags()
        bits = screen.get_bitsize()

        pygame.display.quit()
        pygame.display.init()

        screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
        screen.blit(tmp,(0,0))
        pygame.display.set_caption(*caption)

        pygame.key.set_mods(0) #HACK: work-a-round for a SDL bug??
        self.screen = screen
        return screen