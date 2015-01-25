__author__ = 'joel'

from pygame.locals import *

from resources import *


class Camera(object):

    def __init__(self, target, bounds, size):
        self.bounds = bounds
        self.rect = Rect((0,0), size)

    def update(self, target, SCREEN):
        self.rect.center = target.center
        self.rect = Rect(self.rect.topleft, SCREEN.subsurface((0, 0, SCREEN.get_width(), SCREEN.get_height())).get_size())
        #self.rect.clamp_ip(self.bounds)

    def draw_background(self, surf, bg):
        surf.fill(BLACK)
        bg.draw(surf, self.rect)

    def rel_rect(self, rect, parent):
        return Rect((rect.x - parent.x, rect.y - parent.y), rect.size)

    def drawPlayer(self, surf, player):
        if self.rect.colliderect(player.rect):
            r = self.rel_rect(player.rect, self.rect)
            player.draw(surf, r)
        for a in player.arrows:
            if self.rect.colliderect(a.rect):
                r = self.rel_rect(a.rect, self.rect)
                a.draw(surf, r)

    def drawEnemies(self, surf, enemies):

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                r = self.rel_rect(enemy.rect, self.rect)
                enemy.draw(surf, r)

    def drawHUD(self, player):
        screen = pygame.display.get_surface()
        w,h = screen.get_width(),screen.get_height()
        text = INVFONT.render("arrows: %s, Enemies: %s, Level: %s" % (str(player.inventory[ARROWS]), str(len(ENEMIES)), str(player.level)), True, WHITE, BLACK)

        hud = text.get_rect()
        hud.topleft = [0, h - hud.size[1] - 9]
        screen.blit(text, hud)

        hearts = pygame.Surface((9, 7 * player.hearts))
        for i in range(player.hearts):
            hr = HEART.get_rect()
            hr.topleft = [(i*7), 0]
            hearts.blit(HEART, hr)
        hr = hearts.get_rect()
        hr.topleft = [0, h - hud.size[1]]
        screen.blit(hearts, hr)


    def toggle_fullscreen(self):
        screen = pygame.display.get_surface()
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