__author__ = 'joel'

import json

from pygame import Rect

from resources import *
from Tile import tile

class Map:
    #TODO trap tiles maybe?,
    #TODO different map after lvl 50 to reset creep count (just make stronger monsters and different map to keep the game from exploding from too many enemies),

    tilemap = pygame.sprite.Group()
    def __init__(self, player):
        self.player = player
        f = open("Map/map.json")
        map = json.loads(f.read())
        for cl, row in enumerate(map):
            for rw, t in enumerate(row):
                self.tilemap.add(tile(t, [cl * TILESIZE, rw * TILESIZE]))

    def rel_rect(self, rect, parent):
        return Rect((rect.x - parent.x, rect.y - parent.y), rect.size)

    def draw(self, SCREEN, rect):
        for t in self.tilemap:
            t.draw(SCREEN, self.rel_rect(t.rect, rect))