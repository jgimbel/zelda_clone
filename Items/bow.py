__author__ = 'joel'

from item import Item
from resources import BOW

class bow(Item):
    def __init__(self, topleft=[0,0]):
        super(bow, self).__init__("Sprites/items/bow.png")
        self.rect.topleft = topleft
        self.item = BOW