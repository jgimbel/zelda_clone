__author__ = 'joel'
from item import Item
class shield(Item):
    def __init__(self, inventory=False):
        super(shield, self).__init__("Sprites/items/shield.png", inventory=inventory)
