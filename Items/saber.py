__author__ = 'joel'
from sword import  sword

class saber(sword):
    def __init__(self, topleft=[0,0]):
        super(saber, self).__init__("Sprites/items/sabre1_silver.png", [4, 0],topleft)
        self.damage = 5