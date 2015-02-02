__author__ = 'joel'
import pygame

from item import Item


class bow(Item):
    def __init__(self):
        super(pygame.sprite.Sprite,self).__init__("Sprites/items/bow.png")