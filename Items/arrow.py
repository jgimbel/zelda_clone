__author__ = 'joel'
import pygame
class arrow(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.image = pygame.image.load("sprites/items/arrow.png")