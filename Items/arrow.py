__author__ = 'joel'
from resources import *
class arrow(pygame.sprite.Sprite):

    def __init__(self, face):
        '''

        :return: arrow
        '''
        super(pygame.sprite.Sprite, self).__init__()
        self.image = pygame.image.load("sprites/items/arrow.png").convert()
        self.rect = self.image.get_rect()
        self.direction = face

    def update(self, dt):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if self.direction == UP:
            self.vy = -self.speed
        if self.direction == DOWN:
            self.vy =  self.speed
        if self.direction == LEFT:
            self.vx = -self.speed
        if self.direction == RIGHT:
            self.vx =  self.speed

        if self.vx and self.vy:
            self.vx *= DIAG
            self.vy *= DIAG

        dt /= 1000.0
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
