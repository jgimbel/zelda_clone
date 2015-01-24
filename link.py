__author__ = 'joel'

from pygame.locals import *

from resources import *
from Items import *
from Sprites import *
from Map.Tile import tile


class Player(pygame.sprite.Sprite):
    speed = 125
    resources = [DIRT, GRASS, WATER, COAL]

    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.ss = SpriteSheet('src/player.png')
        self.direction = {
            DOWN: self.ss.image_at((0, 0, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            UP: self.ss.image_at((0, 144, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            RIGHT: self.ss.image_at((0, 96, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            LEFT: self.ss.image_at((0, 48, 32, 48), colorkey=(0, 0, 0)).convert_alpha()

        }
        self.face = DOWN
        self.image = self.direction[self.face]
        self.rect = self.image.get_rect()
        self.rect.topleft = [50, 50]
        self.vx = 0
        self.vy = 0
        self.charge = 0
        self.arrows = pygame.sprite.Group()
        self.equiped = BOW
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

    def swingSword(self):
        self.inventory[SWORD].swordUp(self.charge)
        pygame.sprite.spritecollide(self.inventory[SWORD], ENEMIES, True)
        self.charge = 0

    def shootArrow(self):
        if self.charge > 250:
            self.charge = 250

        if type(self.inventory[BOW]) == bow and self.inventory[ARROWS] > 0:
            self.arrows.add(arrow(self.face, self.rect.center, self.charge))
            self.inventory[ARROWS] -= 1
        self.charge = 0

    def update(self, dt, walls):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            self.vy = -self.speed
            self.face = UP
            self.image = self.direction[self.face]
            self.inventory[SWORD].reverse()

        if keys[K_DOWN]:
            self.vy =  self.speed
            self.face = DOWN
            self.image = self.direction[self.face]
            self.inventory[SWORD].normal()

        if keys[K_LEFT]:
            self.vx = -self.speed
            self.face = LEFT
            self.image = self.direction[self.face]
            self.inventory[SWORD].normal()

        if keys[K_RIGHT]:
            self.vx =  self.speed
            self.face = RIGHT
            self.image = self.direction[self.face]
            self.inventory[SWORD].reverse()

        if keys[K_1]:
            self.equiped = SWORD

        if keys[K_2]:
            self.equiped = BOW

        if keys[K_SPACE]:
            if self.equiped == BOW:
                self.charge += dt
            elif self.equiped == SWORD:
                self.inventory[SWORD].swordDown()
                self.charge += dt
        elif self.charge > 0:
            if self.equiped == BOW:
                self.shootArrow()
            elif self.equiped == SWORD:
                self.swingSword()

        if self.vx and self.vy:
            self.vx *= DIAG
            self.vy *= DIAG


        dt /= 1000.0
        prev_rect = self.rect.copy()
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
        for sprite in pygame.sprite.spritecollide(self, walls, False):
            if type(sprite) == tile:
                if sprite.blocked:
                    # collide with walls
                    rect = sprite.rect
                    if self.rect.left <= rect.right <= prev_rect.left :
                        self.rect.left = rect.right
                    if self.rect.right >= rect.left >= prev_rect.right:
                        self.rect.right = rect.left

                    if self.rect.top <= rect.bottom <= prev_rect.top :
                        self.rect.top = rect.bottom
                    if self.rect.bottom >= rect.top >= prev_rect.bottom:
                        self.rect.bottom = rect.top


        self.arrows.update(dt, walls)
        if self.face == DOWN or self.face == LEFT:
            self.inventory[SWORD].rect = pygame.Rect(self.rect.topleft[0], self.rect.topleft[1] + 15, 16, 16)
        if self.face == UP or self.face == RIGHT:
            self.inventory[SWORD].rect = pygame.Rect(self.rect.topleft[0] + 20, self.rect.topleft[1] + 15, 16, 16)

    def draw(self, SCREEN, rect):
        #Might want to draw the shield behind the player
        if self.face == UP and self.equiped == SWORD:
            if not self.inventory[SWORD].isDown:
                SCREEN.blit(self.inventory[SWORD].image, (rect[0] + 20, rect[1] + 16))
            else:
                SCREEN.blit(self.inventory[SWORD].image, (rect[0] + 20, rect[1] + 22))
            SCREEN.blit(self.inventory[SHIELD].image, (rect[0], rect[1] + 20))

        if self.face == RIGHT and self.equiped == SWORD:
            SCREEN.blit(self.inventory[SHIELD].image, (rect[0]+ 10, rect[1] + 20))

        SCREEN.blit(self.image, rect)
        if type(self.inventory[SWORD]) == sword and self.equiped == SWORD:
            if self.face == DOWN or self.face == LEFT:
                if not self.inventory[SWORD].isDown:
                    SCREEN.blit(self.inventory[SWORD].image, (rect[0], rect[1] + 16))
                else:
                    SCREEN.blit(self.inventory[SWORD].image, (rect[0], rect[1] + 22))

            elif self.face == RIGHT:
                if not self.inventory[SWORD].isDown:
                    SCREEN.blit(self.inventory[SWORD].image, (rect[0] + 16, rect[1] + 16))
                else:
                    SCREEN.blit(self.inventory[SWORD].image, (rect[0] + 16, rect[1] + 22))

            if self.face == LEFT:
                SCREEN.blit(self.inventory[SHIELD].image, (rect[0]+ 10, rect[1] + 20))

            elif self.face == DOWN:
                SCREEN.blit(self.inventory[SHIELD].image, (rect[0]+ 20, rect[1] + 20))


        if type(self.inventory[BOW]) == bow and self.equiped == BOW:
            SCREEN.blit(self.inventory[BOW].image, (rect[0] + 8, rect[1] + 11))