__author__ = 'joel'
import pygame


class sword(pygame.sprite.Sprite):
    def __init__(self):
        super(sword, self).__init__()
        self.image = pygame.image.load("Sprites/items/sword.png")
        self.rect = self.image.get_rect()
        self.direction = 0
        self.isDown = False
    def swordUp(self, charge):
        if self.isDown:
            self.image = pygame.transform.rotate(self.image, -90)
            self.direction -= 90
            self.isDown = False

    def swordDown(self):
        if not self.isDown:
            self.image = pygame.transform.rotate(self.image, 90)
            self.direction += 90
            self.isDown = True
