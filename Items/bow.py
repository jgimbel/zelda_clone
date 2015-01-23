__author__ = 'joel'
import pygame

class bow(pygame.sprite.Sprite):
    def __init__(self):
        super(pygame.sprite.Sprite,self).__init__()
        self.image = pygame.image.load("Sprites/items/bow.png")
        self.rect = self.image.get_rect()