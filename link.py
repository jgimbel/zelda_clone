__author__ = 'joel'

from random import randrange

from pygame.locals import *

from resources import *
from Items import *
from Sprites import *
from Map.Tile import tile
from Items.saber import sword


class Player(pygame.sprite.Sprite):
    speed = 125
    resources = [DIRT, GRASS, WATER, COAL]

    def __init__(self):
        super(Player, self).__init__()
        self.ss = SpriteSheet('src/player.png')
        self.score = 0
        self.level = 1
        self.direction = {
            DOWN: self.ss.image_at((0, 0, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            UP: self.ss.image_at((0, 144, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            RIGHT: self.ss.image_at((0, 96, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            LEFT: self.ss.image_at((0, 48, 32, 48), colorkey=(0, 0, 0)).convert_alpha()

        }
        self.face = DOWN
        self.image = self.direction[self.face]
        self.rect = self.image.get_rect()
        self.rect.topleft = [randrange(0, MAPHEIGHT * TILESIZE), randrange(0, MAPWIDTH * TILESIZE)]
        self.vx = 0
        self.vy = 0
        self.charge = 0
        self.hearts = 20
        self.maxhearts = 20
        self.arrows = pygame.sprite.Group()
        self.equiped = BOW
        self.inventory = {
            SWORD: saber(),
            SHIELD: shield(),
            BOW: bow(),
            ARROWS: 100
        }
    def killed(self):
        self.score += 1
        if self.score % 4 == 0:
            self.level += 1

    def swingSword(self):
        self.inventory[SWORD].swordDown()
        for  enemy in pygame.sprite.spritecollide(self.inventory[SWORD], ENEMIES, False):
            if self.charge < 100:
                enemy.hearts -= 0.5
            else:
                if self.charge > 600:
                    self.charge = 600
                enemy.hearts -= self.charge / 600 * self.inventory[SWORD].damage
            self.inventory[SWORD].s_hit.play()
        else:
            self.inventory[SWORD].s_miss.play(1)
        self.charge = 0

    def shootArrow(self):
        if self.charge > 600:
            self.charge = 600

        if type(self.inventory[BOW]) == bow and self.inventory[ARROWS] > 0:
            tl = self.rect.topleft
            self.arrows.add(arrow(self.face,[tl[0] + 8, tl[1] + 16] , self.charge))
            self.inventory[ARROWS] -= 1
        self.charge = 0

    def update(self, dt, walls):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if self.hearts <= 0:
            self.kill()
            return False

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
                self.inventory[SWORD].swordUp()
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

        if 0 > self.rect.x:
            self.rect.x = 0
        if  self.rect.x > MAPWIDTH * (TILESIZE - 1):
            self.rect.x = MAPWIDTH * (TILESIZE - 1)
        if 0 > self.rect.y:
            self.rect.y = 0
        if  self.rect.y > MAPHEIGHT * (TILESIZE - 1.5):
            self.rect.y = MAPHEIGHT * (TILESIZE - 1.5)


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
        if self.face == UP:
            self.inventory[SWORD].rect.x = self.rect.x
            self.inventory[SWORD].rect.y = self.rect.y + self.inventory[SWORD].handle[1] - 24  - self.rect.size[1]
        if self.face == DOWN:
            self.inventory[SWORD].rect.x = self.rect.x
            self.inventory[SWORD].rect.y = self.rect.y + self.inventory[SWORD].handle[1] + 32 + self.rect.size[1]

        if self.face == RIGHT:
            self.inventory[SWORD].rect.x = self.rect.x + 16  + self.rect.size[0]
            self.inventory[SWORD].rect.y = self.rect.y + self.inventory[SWORD].handle[1]
        if self.face == LEFT:
            self.inventory[SWORD].rect.x = self.rect.x - 16 - self.rect.size[0]
            self.inventory[SWORD].rect.y = self.rect.y + self.inventory[SWORD].handle[1]

        return True

    def draw(self, SCREEN, rect):
        #Might want to draw the shield behind the player
        if self.face == UP and self.equiped == SWORD:
            s = self.inventory[SWORD]
            SCREEN.blit(s.image, (rect[0], rect[1] + s.handle[1] - 24))
            SCREEN.blit(self.inventory[SHIELD].image, (rect[0], rect[1] + 20))

        if self.face == RIGHT and self.equiped == SWORD:
            SCREEN.blit(self.inventory[SHIELD].image, (rect[0]+ 10, rect[1] + 20))

        SCREEN.blit(self.image, rect)

        if issubclass(type(self.inventory[SWORD]), sword) and self.equiped == SWORD:
            s = self.inventory[SWORD]
            if self.face == DOWN:
                SCREEN.blit(s.image, (rect[0], rect[1] + s.handle[1] + 16))
                SCREEN.blit(self.inventory[SHIELD].image, (rect[0]+ 20, rect[1] + 20))
            elif self.face == RIGHT:
                SCREEN.blit(s.image, (rect[0] + 16, rect[1] + s.handle[1]))
            if self.face == LEFT:
                SCREEN.blit(s.image, (rect[0] - 16, rect[1] + s.handle[1]))
                SCREEN.blit(self.inventory[SHIELD].image, (rect[0]+ 10, rect[1] + 20))

        if type(self.inventory[BOW]) == bow and self.equiped == BOW:
            SCREEN.blit(self.inventory[BOW].image, (rect[0] + 8, rect[1] + 11))