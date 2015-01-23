__author__ = 'joel'
import pygame
class arrow(pygame.sprite.Sprite):

    def __init__(self):
        '''

        :return: arrow
        '''
        super(pygame.sprite.Sprite, self).__init__()
        self.image = pygame.image.load("sprites/items/arrow.png").convert()
        self.rect = self.image.get_rect()

    def update(self):
        pass
