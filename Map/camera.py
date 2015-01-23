__author__ = 'joel'

from pygame import Rect

from resources import *


class Camera(object):

    def __init__(self, target, bounds, size):
        self.bounds = bounds
        self.rect = Rect((0,0), size)

    def update(self, target):
        self.rect.center = target.center
        self.rect.clamp_ip(self.bounds)

    def draw_background(self, surf, bg):
        surf.fill(BLACK)
        bg.draw(surf, -self.rect.x, -self.rect.y)

    def rel_rect(rect, parent):
        return Rect((rect.x - parent.x, rect.y - parent.y), rect.size)

    def draw_sprite(self, surf, s):
        if self.rect.colliderect(s.rect):
            surf.blit(s.image, self.rel_rect(s.rect, self.rect))
