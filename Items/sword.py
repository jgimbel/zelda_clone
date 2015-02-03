__author__ = 'joel'
import pygame

from item import Item
from resources import SWORD

class sword(Item):
    def __init__(self, image, handle, topleft=[0,0], inventory=False):
        super(sword, self).__init__(image, inventory=inventory)
        self.type = SWORD
        self.isDown = False
        self.reversed = False
        self.handle = handle
        self.s_miss = pygame.mixer.Sound("Sounds/Effects/battle/swing.ogg")
        self.rect.topleft=topleft
