__author__ = 'joel'
import pygame


class sword(pygame.sprite.Sprite):
    def __init__(self, image, handle):
        super(sword, self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.isDown = False
        self.reversed = False
        self.handle = handle
        self.s_miss = pygame.mixer.Sound("Effects/battle/swing.wav")
        self.s_hit = pygame.mixer.Sound("Effects/NPC/giant/giant1.wav")

    def swordUp(self):
        if self.isDown:
            self.handle[1] -= self.rect.size[1]
            if self.reversed:
                self.image = pygame.transform.rotate(self.image, 90)
            else:
                self.image = pygame.transform.rotate(self.image, -90)
            self.isDown = False

    def swordDown(self):
        if not self.isDown:
            self.handle[1] += self.rect.size[1]
            if self.reversed:
                self.image = pygame.transform.rotate(self.image, -90)
            else:
                self.image = pygame.transform.rotate(self.image, 90)
            self.isDown = True

    def reverse(self):
        if not self.reversed:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.reversed = True

    def normal(self):
        if self.reversed:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.reversed = False
