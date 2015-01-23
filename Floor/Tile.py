__author__ = 'joel'
from resources import *
class tile(pygame.sprite.Sprite):


    def __init__(self, type, tl):
        super(tile, self).__init__()
        self.image = textures[type]
        self.rect = self.image.get_rect()
        self.rect.topleft = tl