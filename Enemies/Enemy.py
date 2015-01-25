__author__ = 'joel'
from pygame import Rect

from resources import *
from Map.Tile import tile


class enemy(pygame.sprite.Sprite):
    speed = 100
    hearts = 5.0
    def __init__(self, sprite, x, y):
        pygame.sprite.Sprite.__init__(self, ENEMIES)
        self.sheet = sprite
        self.direction = {
            DOWN: self.sheet.image_at((0, 0, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            UP: self.sheet.image_at((0, 144, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            RIGHT: self.sheet.image_at((0, 96, 32, 48), colorkey=(0, 0, 0)).convert_alpha(),
            LEFT: self.sheet.image_at((0, 48, 32, 48), colorkey=(0, 0, 0)).convert_alpha()
        }
        self.image = self.direction[DOWN]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.attacking = False
        self.attack_length = 0

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
        player.score += 1
        if player.score % 2 == 0:
            player.level += 1


    def update(self, target, dt, weapons, walls, player):
        if self.hearts <= 0:
            self.kill(player)


        if self.attack_length > 0:
            self.attack_length -= 1
            return

        for col in pygame.sprite.spritecollide(self, weapons, True):
            self.hearts -= col.speed / 50

        d = self.rect.x - target.rect.x, self.rect.y - target.rect.y
        t = self.normalize_vector(d[0] ,d[1])

        dt /= 1000.0
        prev_rect = self.rect.copy()
        self.rect.x -= t[0] * self.speed * dt
        self.rect.y -= t[1] * self.speed * dt

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

                    player.hearts -= 0.5

    def draw(self, SCREEN, rect):
        if self.hearts > 0:
            pygame.draw.rect(SCREEN,(255,0,0), Rect(rect.x - 2, rect.y - 5, 5 * self.hearts, 5))
        SCREEN.blit(self.image, rect)