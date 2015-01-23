__author__ = 'joel'

from pygame.locals import *

from resources import *
from Items import *



class Player(pygame.sprite.Sprite):
    speed = 125
    resources = [DIRT, GRASS, WATER, COAL]
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.image = pygame.image.load('player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        self.vx = 0
        self.vy = 0
        self.face = DOWN
        self.showBow = False
        self.charge = 0
        self.arrows = pygame.sprite.Group()
        self.inventory = {
            DIRT: 0,
            GRASS: 0,
            WATER: 0,
            COAL: 0,
            SWORD: sword(),
            SHIELD: shield(),
            BOW: bow(),
            ARROWS: 100
        }

    def shootArrow(self):

        if self.charge > 50:
            self.charge = 50

        if type(self.inventory[BOW]) == bow and self.inventory[ARROWS] > 0:
            self.arrows.add(arrow(self.face, self.rect.topleft, self.charge))
            self.charge = 0
            self.inventory[ARROWS] -= 1


    def update(self, dt):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            self.vy = -self.speed
            self.face = UP
            self.showBow = False
        if keys[K_DOWN]:
            self.vy =  self.speed
            self.face = DOWN
            self.showBow = True
        if keys[K_LEFT]:
            self.vx = -self.speed
            self.face = LEFT
            self.showBow = False
        if keys[K_RIGHT]:
            self.vx =  self.speed
            self.face = RIGHT
            self.showBow = False

        if keys[K_SPACE]:
            self.charge += dt
        elif self.charge > 0:
            self.shootArrow()

        if self.vx and self.vy:
            self.vx *= DIAG
            self.vy *= DIAG


        dt /= 1000.0
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        self.arrows.update(dt)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)
        self.arrows.draw(SCREEN)

        if type(self.inventory[SWORD]) == sword and (self.face == DOWN or self.face == RIGHT) and self.charge == 0:
            SCREEN.blit(self.inventory[SWORD].image, (self.rect.topleft[0], self.rect.topleft[1] + 10))

        if type(self.inventory[SHIELD]) == shield and (self.face == DOWN or self.face == LEFT) and self.charge == 0:
            SCREEN.blit(self.inventory[SHIELD].image, (self.rect[0] + 10, self.rect[1] + 14))

        if type(self.inventory[BOW]) == bow and (self.face == UP or self.charge > 0):
            SCREEN.blit(self.inventory[BOW].image, (self.rect[0] + 8, self.rect[1] + 11))

        '''
        placePosition = 10
        for item in self.resources:
            SCREEN.blit(textures[item], (placePosition, MAPHEIGHT * TILESIZE + 20))
            placePosition += 30
            textObj = INVFONT.render(str(self.inventory[item]), True, WHITE, BLACK)
            SCREEN.blit(textObj, (placePosition, MAPHEIGHT * TILESIZE + 20))
            placePosition += 50
        '''