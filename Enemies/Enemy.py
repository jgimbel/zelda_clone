__author__ = 'joel'
from random import randrange

from pygame import Rect

from resources import *
from Map.Tile import tile
from Items.saber import saber
from Items.bow import bow
from Items.arrow import arrow
from Items.heart import heart

class enemy(pygame.sprite.Sprite):
    #TODO different enemies,
    speed = 100
    hearts = 5.0
    moveWait = 0
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self, ENEMIES)
        self.ss = sprite
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
        self.face = UP
        self.image = self.direction[self.face]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.attacking = False
        self.attack_length = 0
        self.foot = LEFT_FOOT
        self.foundPlayer = False
        self.hit = pygame.mixer.Sound("Sounds/Effects/NPC/giant/giant1.ogg")

    def attack(self):
        self.attack_length = 12

    def vector_length(self, x, y):
        return math.sqrt(x*x + y*y)

    def normalize_vector(self, x, y):
        norm = self.vector_length(x, y)
        if norm == 0:
            return 0, 0
        return x/norm, y/norm

    def kill(self, player):
        super(enemy, self).kill()
        item = randrange(0,100)
        if item < 40:
            ITEMS.add(arrow(self.rect.topleft))
            if item < 20:
                ITEMS.add(arrow(self.rect.topleft))
                if item < 10:
                    ITEMS.add(arrow(self.rect.topleft))

        elif 40  < item <= 60:
            ITEMS.add(bow(self.rect.topleft))
        elif 60 < item <= 80:
            ITEMS.add(saber(self.rect.topleft))
        else:
            ITEMS.add(heart(self.rect.topleft))

    def collideWall(self, walls, prev_rect):
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

    def tryAttack(self,player, prev_rect):
         if pygame.sprite.collide_rect(self, player):
                if not self.attacking:
                    self.attack()
                    rect = player.rect
                    if self.rect.left <= rect.right <= prev_rect.left :
                        self.rect.left = rect.right
                    if self.rect.right >= rect.left >= prev_rect.right:
                        self.rect.right = rect.left

                    if self.rect.top <= rect.bottom <= prev_rect.top :
                        self.rect.top = rect.bottom
                    if self.rect.bottom >= rect.top >= prev_rect.bottom:
                        self.rect.bottom = rect.top

                    player.hearts -= 1

    def moveEnemy(self, target, dt):
        if self.foundPlayer:
            t = self.movePlayer(target)
        else:
            t = self.moveRandom(target)

        self.image = self.direction[self.face]
        t = (t[0] * self.speed * dt / 1000, t[1] * self.speed * dt / 1000)
        self.rect.x -= t[0]
        self.rect.y -= t[1]

        if 0 > self.rect.x:
            self.rect.x = 0
        if  self.rect.x > MAPWIDTH * TILESIZE:
            self.rect.x = MAPWIDTH * TILESIZE
        if 0 > self.rect.y:
            self.rect.y = 0
        if  self.rect.y > MAPHEIGHT * (TILESIZE - 1):
            self.rect.y = MAPHEIGHT * (TILESIZE - 1)

        if t[0] != 0 or t[1] != 0:
            self.image = self.direction[self.face + self.foot]
            self.foot = ((self.foot + 1) % 4)
        else:
            self.image = self.direction[self.face]

    def moveRandom(self, target):
        if self.moveWait < randrange(20, 90):
            self.moveWait += 1
            return 0,0
        else:
            self.moveWait = 0
        nextFace = randrange(1,10,1)
        t = (0,0)
        if 1<= nextFace < 2:
            if self.face == UP:
                t = (0,1)
            if self.face == DOWN:
                t = (0,-1)
            if self.face == RIGHT:
                t = (1,0)
            if self.face == LEFT:
                t = (-1,0)
        if 2 <= nextFace < 4:
            if self.face == UP:
                t = (-1,0)
            if self.face == DOWN:
                t = (1,0)
            if self.face == RIGHT:
                t = (0,-1)
            if self.face == LEFT:
                t = (0,1)
        if 4 <= nextFace < 6:
            if self.face == UP:
                t = (1,0)
            if self.face == DOWN:
                t = (-1,0)
            if self.face == RIGHT:
                t = (0,1)
            if self.face == LEFT:
                t = (0,-1)
        if 6 <= nextFace < 8:
            if self.face == UP:
                t = (0,-1)
            if self.face == DOWN:
                t = (0,1)
            if self.face == RIGHT:
                t = (-1,0)
            if self.face == LEFT:
                t = (1,0)

        dist = math.sqrt((self.rect.x - target.rect.x)**2 + (self.rect.y - target.rect.y)**2)
        if abs(t[0]) > abs(t[1]):
            if t[0] > 0:
                self.face = LEFT
                if dist < CAMHEIGHT*TILESIZE/2 and target.rect.y - 10 <= self.rect.y <= target.rect.y + 10 and target.rect.x < self.rect.x:
                    self.foundPlayer = True
            else:
                self.face = RIGHT
                if dist < CAMHEIGHT*TILESIZE/2 and target.rect.y - 10 <= self.rect.y <= target.rect.y + 10 and target.rect.x > self.rect.x:
                    self.foundPlayer = True
        else:
            if t[1] > 0:
                self.face = UP
                if dist < CAMHEIGHT*TILESIZE/2 and target.rect.x - 10 <= self.rect.x <= target.rect.x + 10 and target.rect.y < self.rect.y:
                    self.foundPlayer = True
            else:
                self.face = DOWN
                if dist < CAMHEIGHT*TILESIZE/2 and target.rect.x - 10 <= self.rect.x <= target.rect.x + 10 and target.rect.y > self.rect.y:
                    self.foundPlayer = True

        return t

    def movePlayer(self, target):
        d = self.rect.x - target.rect.x, self.rect.y - target.rect.y
        t = self.normalize_vector(d[0] ,d[1])
        if abs(t[0]) > abs(t[1]):
            if t[0] > 0:
                self.face = LEFT
            else:
                self.face = RIGHT
        else:
            if t[1] > 0:
                self.face = UP
            else:
                self.face = DOWN

        return t

    def update(self, target, dt, walls):
        if self.attack_length > 0:
            self.attack_length -= 1
            return


        for a in pygame.sprite.spritecollide(self, target.arrows, True):
            self.hearts -= a.speed / 100
            self.foundPlayer = True

        if self.hearts <= 0:
            self.kill(target)

        prev_rect = self.rect.copy()
        self.moveEnemy(target, dt)

        self.collideWall(walls, prev_rect)
        self.tryAttack(target, prev_rect)

    def draw(self, SCREEN, rect):
        if self.hearts > 0:
            pygame.draw.rect(SCREEN,(255,0,0), Rect(rect.x + 2, rect.y - 5, 5 * self.hearts, 5))
        SCREEN.blit(self.image, rect)