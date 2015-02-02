__author__ = 'joel'
import pygame

from resources import ITEMS


class Item(pygame.sprite.Sprite):

    def __init__(self, image):
        self.timeToDesync = 0
        self.inInventory = False
        super(Item, self).__init__(ITEMS)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        if not self.inInventory:

            if self.timeToDesync > 60:
                self.kill()

            self.timeToDesync += 1
    def draw(self, screen, rect):
        screen.blit(self.image, rect)