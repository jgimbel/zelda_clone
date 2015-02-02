__author__ = 'joel'
from item import Item
class heart(Item):
    def __init__(self, topleft=[0,0]):
        super(heart, self).__init__("src/heart.png", topleft=topleft)