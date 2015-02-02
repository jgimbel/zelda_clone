__author__ = 'joel'

from pygame.locals import *

from resources import *


class Camera(object):

    def __init__(self, target, bounds, size, h, w):
        self.bounds = bounds
        self.rect = Rect((0,0), size)
        self.fullscreen = False
        self.FULLH = h
        self.FULLW = w

    def update(self, target, SCREEN):
        self.rect.center = target.center
        self.rect = Rect(self.rect.topleft, SCREEN.subsurface((0, 0, SCREEN.get_width(), SCREEN.get_height())).get_size())
        #self.rect.clamp_ip(self.bounds)

    def draw_background(self, surf, bg):
        surf.fill(BLACK)
        bg.draw(surf, self.rect)

    def draw_pause(self, surf):
        w,h = surf.get_width(),surf.get_height()
        text = INVFONT.render("PAUSED", True, WHITE, BLACK)

        hud = text.get_rect()
        hud.topleft = [w/2 - + hud.size[0] / 2, h/2 - 38]
        surf.blit(text, hud)


    def rel_rect(self, rect, parent):
        return Rect((rect.x - parent.x, rect.y - parent.y), rect.size)

    def drawPlayer(self, surf, player):
        if self.rect.colliderect(player.rect):
            r = self.rel_rect(player.rect, self.rect)
            player.draw(surf, r)
        for a in player.inventory[ARROWS]:
            if self.rect.colliderect(a.rect):
                r = self.rel_rect(a.rect, self.rect)
                a.draw(surf, r)

    def drawEnemies(self, surf, enemies):

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                r = self.rel_rect(enemy.rect, self.rect)
                enemy.draw(surf, r)

    def drawHUD(self, player, wave):
        #TODO: make counter to when the next wave starts
        screen = pygame.display.get_surface()
        w,h = screen.get_width(),screen.get_height()
        text = INVFONT.render("arrows: %s, Enemies: %s, Wave: %s" % (str(len(player.inventory[ARROWS])), str(len(ENEMIES)), str(wave)), True, WHITE, BLACK)

        hud = text.get_rect()
        hud.topleft = [0, h - hud.size[1] - 9]
        screen.blit(text, hud)

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
        screen.blit(hearts.convert_alpha(), hr)


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

        return screen