__author__ = 'joel'
from sword import  sword

class dagger(sword):
    def __init__(self):
        super(dagger, self).__init__("Sprites/items/sword.png", [22, 16])
        self.damage = 1