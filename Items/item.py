__author__ = 'joel'

from resources import *


class Item(pygame.sprite.Sprite):

    #TODO different weapons (throwing star, boomerang, etc.),
    def __init__(self, image, inventory=False, topleft=[0,0]):
        self.type = ITEM
        if not inventory:
            super(Item, self).__init__(ITEMS)
        else:
            super(Item, self).__init__()

        self.timeToDesync = 0
        self.inInventory = inventory
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.reversed = False

    def update(self):
        if not self.inInventory:

            if self.timeToDesync > 60000:
                self.kill()

            self.timeToDesync += 1

    def draw(self, screen, rect):
        screen.blit(self.image, rect)

    def reverse(self):
        if not self.reversed:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.reversed = True

    def normal(self):
        if self.reversed:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.reversed = False

    def up(self):
        if self.isDown:
            self.handle[1] -= self.rect.size[1]
            if self.reversed:
                self.image = pygame.transform.rotate(self.image, 90)
            else:
                self.image = pygame.transform.rotate(self.image, -90)
            self.isDown = False

    def down(self):
        if not self.isDown:
            self.handle[1] += self.rect.size[1]
            if self.reversed:
                self.image = pygame.transform.rotate(self.image, -90)
            else:
                self.image = pygame.transform.rotate(self.image, 90)
            self.isDown = True