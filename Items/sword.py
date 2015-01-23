__author__ = 'joel'
import pygame


class sword(pygame.sprite.Sprite):
    def __init__(self):
        super(sword, self).__init__()
        self.image = pygame.image.load("sprites/items/sword.png")
        self.rect = self.image.get_rect()
        self.direction = 0
    def swordUp(self, charge):
        if self.direction == 90:
            self.image = pygame.transform.rotate(self.image, -90)
            self.direction -= 90

    def swordDown(self):
        if self.direction == 0:
            self.image = pygame.transform.rotate(self.image, 90)
            self.direction += 90