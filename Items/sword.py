__author__ = 'joel'
import pygame


class sword(pygame.sprite.Sprite):
    def __init__(self):
        super(sword, self).__init__()
        self.image = pygame.image.load("sprites/items/sword.png")
        self.rect = self.image.get_rect()