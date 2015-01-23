__author__ = 'joel'
from resources import *
class arrow(pygame.sprite.Sprite):
    def __init__(self, face, tl, charge):
        '''

        :return: arrow
        '''
        super(arrow, self).__init__()
        self.image = pygame.image.load("sprites/items/arrow.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = tl
        self.direction = face
        self.vx = 0
        self. vy = 0
        self.distance = 0
        self.speed = charge
        if self.direction == UP:
            self.vy = -self.speed
            self.image = pygame.transform.rotate(self.image, 45)
        if self.direction == DOWN:
            self.vy = self.speed
            self.image = pygame.transform.rotate(self.image, 225)
        if self.direction == LEFT:
            self.vx = -self.speed
            self.image = pygame.transform.rotate(self.image, 135)
        if self.direction == RIGHT:
            self.vx = self.speed
            self.image = pygame.transform.rotate(self.image, 315)

    def update(self, dt):
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        self.distance += dt
        self.speed -= 10
        if self.distance > self.speed:
            self.kill()