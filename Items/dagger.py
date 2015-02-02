__author__ = 'joel'
from sword import  sword

class dagger(sword):
    def __init__(self, inventory=False):
        super(dagger, self).__init__("Sprites/items/sword.png", [22, 16], inventory=inventory)
        self.damage = 1