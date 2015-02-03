__author__ = 'joel'
import pygame

from resources import BLACK, WHITE, ITEMS, INVFONT
from arrow import arrow


class Backpack():
    def __init__(self):
        self.sizeX = 5
        self.sizeY = 5
        self.inventory = [[None for w in range(self.sizeX)] for h in range(self.sizeY)]
        self.toolbar = [None for x in range(self.sizeX)]
        self.inventory[0][0] = pygame.sprite.Group(arrow([0,0]))



    def addInventory(self, item, x=None,y=None):
        if type(item) == arrow:
            self.inventory[0][0].add(item)
        if x != None and y != None:
            r = self.inventory[x][y]
            self.inventory[x][y] = item
            return r
        else:
            for vx in range(self.sizeX):
                for vy in range(self.sizeY):
                    if self.inventory[vx][vy]:
                        r = self.inventory[vx][vy]
                        self.inventory[vx][vy] = item
                        return r

                    r = self.inventory[4][4]
                    self.inventory[4][4] = item
                    return r

    def addToolbar(self, item, x=None):
        if x:
            r = self.inventory[x]
            self.inventory[x] = item
            return r
        else:
            for vx in range(self.sizeX):
                if not self.inventory[vx]:
                    r = self.inventory[vx]
                    self.inventory[vx] = item
                    return r
            return self.addInventory(item)

    def drop(self, item, rect):
        ITEMS.add(item)
        item.rect = rect

    def draw(self, screen):
        w, h = screen.get_size()
        disp = pygame.surface.Surface((204,204))
        disp.fill(BLACK)
        empty = pygame.surface.Surface((32, 32))
        empty.fill(WHITE)
        x, y = 4, 4
        for i in self.inventory:
            for item in i:
                if item:
                    disp.blit(item.image, [x, y])
                else:
                    disp.blit(empty, [x, y])
                x += 32
            y += 32
            x = 4

        disp.blit(self.inventory[0][0].sprites()[0], [4, 4])
        disp.blit(INVFONT.render(str(len(self.inventory[0][0].sprites()[0])), True, WHITE, BLACK), [4, 4])

        y += 8
        for item in self.toolbar:
            if item:
                disp.blit(item.image, [x, y])
            else:
                disp.blit(empty, [x, y])
            x += 32
        screen.blit(disp, [w/2-45, h/2-47])

    def __getitem__(self, item):
        for i in self.toolbar:
            if i and i.item == item:
                return i

        for items in self.inventory:
            for i in items:
                if i and i.item == item:
                    return i

        return None
