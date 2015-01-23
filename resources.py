__author__ = 'joel'

import pygame, sys

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.font.init()
INVFONT = ""
if sys.platform == "linux" or sys.platform == "linux2":
    INVFONT = pygame.font.Font("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 18)

elif sys.platform == "win32":
    INVFONT = pygame.font.Font("C:\Windows\Fonts\calibrib.ttf", 18)

TILESIZE = 32
MAPWIDTH = 10
MAPHEIGHT =10

#colors
BLACK = (0,0,0)
BROWN = (153, 76, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

textures = {
	DIRT : pygame.image.load('4_earthTiles/38earth8.bmp'),
	GRASS: pygame.image.load('1_grassTiles/1grass1.bmp'),
	WATER: pygame.image.load('2_waterTiles/13water3.bmp'),
	COAL : pygame.image.load('4_earthTiles/32earth2.bmp')
	}

resources = [DIRT, GRASS, WATER, COAL]
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]


