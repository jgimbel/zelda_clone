__author__ = 'joel'
from resources import *
from Map.Tile import tile
from item import Item
class arrow(Item):
    direction = ""
    speed = 0
    distance = 0
    vx = 0
    vy = 0
    def __init__(self, tl):
        super(arrow, self).__init__("Sprites/items/arrow.png")
        self.item = ARROW
        self.rect.topleft = tl


    def shoot(self, face, tl, charge):
        self.rect.topleft = tl
        self.direction = face
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

    def update(self, dt, walls):
        super(arrow, self).update()
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        self.distance += dt
        self.speed -= 10
        if self.distance > self.speed:
            self.kill()
        for sprite in pygame.sprite.spritecollide(self, walls, False):
            if type(sprite) == tile and sprite.blocked:
                self.kill()

    def draw(self, SCREEN, rect):
        super(arrow, self).draw(SCREEN, rect)