__author__ = 'joel'
import pygame
from resources import *

class Player(pygame.sprite.Sprite):

	def __init__(self):
		super(pygame.sprite.Sprite, self).__init__()
		self.image = pygame.image.load('player.png').convert_alpha()
		self.Pos = [0, 0]
		self. inventory = {
			DIRT: 0,
			GRASS: 0,
			WATER: 0,
			COAL: 0,
			SWORD: False,
			SHIELD: False,
			BOW: False
		}
