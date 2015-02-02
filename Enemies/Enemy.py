__author__ = 'joel'
from pygame import Rect

from resources import *
from Map.Tile import tile


class enemy(pygame.sprite.Sprite):
    #TODO different enemies,
    speed = 100
    hearts = 5.0
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
        player.killed()


    def update(self, target, dt, walls, player):

        for arrow in pygame.sprite.spritecollide(self, player.inventory[ARROWS], True):
            self.hearts -= arrow.speed / 100

        if self.hearts <= 0:
            self.kill(player)
        #TODO Drops from peeps,


        #TODO epic monsters on % 5 levels,
        #TODO super monsters on % 10 levels (still gets other bosses from % 5),
        if self.attack_length > 0:
            self.attack_length -= 1
            return

        d = self.rect.x - target.rect.x, self.rect.y - target.rect.y
        t = self.normalize_vector(d[0] ,d[1])

        dt /= 1000.0
        prev_rect = self.rect.copy()

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

        self.image = self.direction[self.face]
        self.rect.x -= t[0] * self.speed * dt
        self.rect.y -= t[1] * self.speed * dt

        if t[0] != 0 or t[1] != 0:
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



    def draw(self, SCREEN, rect):
        if self.hearts > 0:
            pygame.draw.rect(SCREEN,(255,0,0), Rect(rect.x + 2, rect.y - 5, 5 * self.hearts, 5))
        SCREEN.blit(self.image, rect)