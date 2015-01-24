__author__ = 'joel'
from resources import *


class tile(pygame.sprite.Sprite):
    def __init__(self, type, tl):
        super(tile, self).__init__()
        self.image = textures[type]
        self.blocked = False
        if type == COAL:
            self.blocked = True
        self.rect = self.image.get_rect()
        self.rect.topleft = tl

    def draw(self,SCREEN, rect):
        SCREEN.blit(self.image, rect)