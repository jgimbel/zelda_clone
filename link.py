__author__ = 'joel'

from random import randrange

from pygame.locals import *

from resources import *
from Items import *
from Sprites import *
from Map.Tile import tile
from Items.saber import sword


class Player(pygame.sprite.Sprite):
    #TODO crafting system,
    #TODO UI for building/placing items,
    speed = 125
    resources = [DIRT, GRASS, WATER, COAL, arrow]

    def __init__(self):
        super(Player, self).__init__()
        self.ss = SpriteSheet('src/player.png')
        self.score = 0
        self.direction = {
            DOWN: self.ss.image_at((0, 0, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            UP: self.ss.image_at((0, 144, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            RIGHT: self.ss.image_at((0, 96, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            LEFT: self.ss.image_at((0, 48, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),

            DOWN + RIGHT_FOOT: self.ss.image_at((32, 0, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            UP + RIGHT_FOOT: self.ss.image_at((32, 144, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            RIGHT + RIGHT_FOOT: self.ss.image_at((32, 96, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            LEFT + RIGHT_FOOT: self.ss.image_at((32, 48, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),


            DOWN + CENTER: self.ss.image_at((64, 0, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            UP + CENTER: self.ss.image_at((64, 144, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            RIGHT + CENTER: self.ss.image_at((64, 96, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            LEFT + CENTER: self.ss.image_at((64, 48, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),

            DOWN + LEFT_FOOT: self.ss.image_at((96, 0, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            UP + LEFT_FOOT: self.ss.image_at((96, 144, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            RIGHT + LEFT_FOOT: self.ss.image_at((96, 96, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            LEFT + LEFT_FOOT: self.ss.image_at((96, 48, 32, 48), colorkey=(0, 0, 0)).convert_alpha()
        }
        self.face = DOWN
        self.image = self.direction[self.face]
        self.rect = self.image.get_rect()
        self.rect.topleft = [randrange(0, MAPHEIGHT * TILESIZE), randrange(0, MAPWIDTH * TILESIZE)]
        vx = 0
        vy = 0
        self.charge = 0
        self.hearts = 20
        self.maxhearts = 20

        self.arrows = pygame.sprite.Group()
        self.inventory = Backpack()
        self.inventory.addToolbar(dagger(True), 0)
        #self.inventory.addToolbar(saber())

        self.equiped = self.inventory[DAGGER]
        self.foot = LEFT_FOOT

    def swingSword(self):
        self.equiped.down()
        for  enemy in pygame.sprite.spritecollide(self.equiped, ENEMIES, False):
            if self.charge < 100:
                enemy.hearts -= 0.5
            else:
                if self.charge > 600:
                    self.charge = 600
                enemy.hearts -= self.charge / 600 * self.equiped.damage
                enemy.hit.play()
        else:
            self.equiped.s_miss.play()
        self.charge = 0

    def shootArrow(self):
        if self.charge > 600:
            self.charge = 600
        if self.inventory[ARROW] is not None:
            tl = self.rect.topleft
            a = self.inventory.drop(ARROW)
            self.arrows.add(a)
            a.shoot(self.face, [tl[0] + 8, tl[1] + 16], self.charge)
        self.charge = 0

    def update(self, dt, walls):
        """

        :type self: Player
        :type dt: int
        :type walls: pygame.sprite.Group
        """
        if self.hearts <= 0:
            self.kill()
            return False
        vx, vy = 0, 0
        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            vy = -self.speed
            self.face = UP
            self.equiped.reverse()

        if keys[K_DOWN]:
            vy =  self.speed
            self.face = DOWN
            self.equiped.normal()

        if keys[K_LEFT]:
            vx = -self.speed
            self.face = LEFT
            self.equiped.normal()

        if keys[K_RIGHT]:
            vx =  self.speed
            self.face = RIGHT
            self.equiped.reverse()

        if keys[K_1]:
            if self.inventory.toolbar[0].type is not None and self.inventory.toolbar[0].type != ARROW:
                self.equiped = self.inventory.toolbar[0].sprites()[0]

        if keys[K_2]:
            if self.inventory.toolbar[1].type is not None and self.inventory.toolbar[0].type != ARROW:
                self.equiped = self.inventory.toolbar[1].sprites()[0]

        if keys[K_3]:
            if self.inventory.toolbar[2].type is not None and self.inventory.toolbar[0].type != ARROW:
                self.equiped = self.inventory.toolbar[2].sprites()[0]

        if keys[K_4]:
            if self.inventory.toolbar[3].type is not None and self.inventory.toolbar[0].type != ARROW:
                self.equiped = self.inventory.toolbar[3].sprites()[0]

        if keys[K_5]:
            if self.inventory.toolbar[4].type is not None and self.inventory.toolbar[0].type != ARROW:
                self.equiped = self.inventory.toolbar[4].sprites()[0]

        if keys[K_SPACE]:
            if type(self.equiped) == bow:
                self.charge += dt

            elif issubclass(type(self.equiped), sword):
                self.equiped.up()
                self.charge += dt

        elif self.charge > 0:
            if type(self.equiped) == bow:
                self.shootArrow()
            elif issubclass(type(self.equiped), sword):
                self.swingSword()

        if vx and vy:
            vx *= DIAG
            vy *= DIAG


        dt /= 1000.0
        prev_rect = self.rect.copy()
        self.rect.x += vx * dt
        self.rect.y += vy * dt

        if 0 > self.rect.x:
            self.rect.x = 0
        if  self.rect.x > MAPWIDTH * (TILESIZE-1):
            self.rect.x = MAPWIDTH * (TILESIZE-1)
        if 0 > self.rect.y:
            self.rect.y = 0
        if  self.rect.y > MAPHEIGHT * (TILESIZE - 1):
            self.rect.y = MAPHEIGHT * (TILESIZE - 1)

        if vx != 0 or vy != 0:
            self.image = self.direction[self.face + self.foot]
            self.foot = ((self.foot + 1) % 4)
        else:
            self.image = self.direction[self.face]

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

        for i in pygame.sprite.spritecollide(self, ITEMS, True):
            if issubclass(type(i), sword) or type(i) == bow or type(i) == arrow:
                self.inventory.addToolbar(i)
            elif type(i) == heart:
                if self.hearts < self.maxhearts:
                    self.hearts += 2


        if self.face == UP:
            self.equiped.rect.x = self.rect.x
            self.equiped.rect.bottom = self.rect.top - 32
        if self.face == DOWN:
            self.equiped.rect.x = self.rect.x
            self.equiped.rect.top = self.rect.bottom
        if self.face == RIGHT:
            self.equiped.rect.left = self.rect.right
            self.equiped.rect.y = self.rect.y
        if self.face == LEFT:
            self.equiped.rect.right = self.rect.left - 32
            self.equiped.rect.y = self.rect.y
        return True

    def draw(self, SCREEN, rect):
        #Might want to draw the shield behind the player

        SCREEN.blit(self.image, rect)

        if issubclass(type(self.equiped), sword):
            s = self.equiped
            if self.face == UP:
                SCREEN.blit(s.image, (rect[0], rect.top-32))
            if self.face == DOWN:
                SCREEN.blit(s.image, (rect[0], rect.bottom))
            if self.face == RIGHT:
                SCREEN.blit(s.image, (rect.right, rect[1]))
            if self.face == LEFT:
                SCREEN.blit(s.image, (rect.left-32, rect[1]))

        if type(self.equiped) == bow:
            SCREEN.blit(self.inventory[BOW].image, (rect[0] + 8, rect[1] + 11))