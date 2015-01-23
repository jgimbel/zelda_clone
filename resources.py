__author__ = 'joel'

import sys
import math

import pygame
DIAG = 1 / math.sqrt(2)
DOWN = 0
UP = 1
RIGHT = 2
LEFT = 3

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

SWORD = "sword"
BOW = "bow"
SHIELD = "shield"


fpsClock = pygame.time.Clock()
pygame.font.init()
INVFONT = ""
if sys.platform == "linux" or sys.platform == "linux2":
    INVFONT = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 18)

elif sys.platform == "win32" or sys.platform == "cygwin":
    INVFONT = pygame.font.Font("C:\Windows\Fonts\calibrib.ttf", 18)

# colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)