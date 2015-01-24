__author__ = 'joel'
from resources import *
class tile(pygame.sprite.Sprite):
    def __init__(self, type, tl):
        super(tile, self).__init__()
        self.image = textures[type]
        self.blocked = False

        self.rect = self.image.get_rect()
        self.rect.topleft = tl

        self.place = tl

    def update(self, x, y):
        self.rect.x =  self.place[0] + x - (MAPHEIGHT * TILESIZE/2)
        self.rect.y =  self.place[1] + y - (MAPWIDTH * TILESIZE/2)