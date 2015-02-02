__author__ = 'joel'

import sys
import math

import pygame


DIAG = 1 / math.sqrt(2)

LEFT_FOOT = 1
CENTER = 2
RIGHT_FOOT = 3

DOWN = 0
UP = 4
RIGHT = 8
LEFT = 12

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

TILESIZE = 32
MAPWIDTH = 60
MAPHEIGHT = 60
CAMHEIGHT = 10
CAMWIDTH = 10
SCORE = 0

SWORD = "sword"
BOW = "bow"
SHIELD = "shield"
ARROWS = "arrows"
QUIVER = "quiver"
textures = {
    DIRT: pygame.image.load('Sprites/earthTiles/38earth8.bmp'),
    GRASS: pygame.image.load('Sprites/grassTiles/1grass1.bmp'),
    WATER: pygame.image.load('Sprites/waterTiles/13water3.bmp'),
    COAL: pygame.image.load('Sprites/earthTiles/32earth2.bmp')
}
pygame.font.init()
INVFONT = ""
if sys.platform == "linux" or sys.platform == "linux2":
    INVFONT = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 14)

elif sys.platform == "win32" or sys.platform == "cygwin":
    INVFONT = pygame.font.Font("C:\Windows\Fonts\calibrib.ttf", 14)

# colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
HEART = pygame.image.load('Sprites/heart.png')
EMPTY_HEART = pygame.image.load('Sprites/heart_empty.png')
ENEMIES = pygame.sprite.Group()
ITEMS = pygame.sprite.Group()

LEVEL = 1