__author__ = 'joel'
from resources import *
class tile(pygame.sprite.Sprite):


    def __init__(self, type, tl):
        super(tile, self).__init__()
        self.image = textures[type]

        self.rect = self.image.get_rect()
        self.rect.topleft = tl

        self.place = self.image.get_rect()

    def update(self, x, y):
        self.rect.x = self.place.x + x
        self.rect.y = self.place.y + y