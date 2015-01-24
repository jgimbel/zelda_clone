__author__ = 'joel'

from pygame import Rect

from resources import *


class Camera(object):

    def __init__(self, target, bounds, size):
        self.bounds = bounds
        self.rect = Rect((0,0), size)

    def update(self, target):
        self.rect.center = target.center
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