__author__ = 'joel'

import pygame, sys
import random
from pygame.locals import *

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.font.init()
INVFONT = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 18)

TILESIZE = 64
MAPWIDTH = 10
MAPHEIGHT =10