__author__ = 'joel'

from resources import *


class Item(pygame.sprite.Sprite):

    #TODO different weapons (throwing star, boomerang, etc.),
    def __init__(self, image, inventory=False):
        if not inventory:
            super(Item, self).__init__(ITEMS)
        else:
            super(Item, self).__init__()

        self.timeToDesync = 0
        self.inInventory = inventory
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        if not self.inInventory:

            if self.timeToDesync > 60000:
                self.kill()

            self.timeToDesync += 1
    def draw(self, screen, rect):
        screen.blit(self.image, rect)