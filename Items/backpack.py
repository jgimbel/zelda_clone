__author__ = 'joel'
import pygame

from resources import BLACK, WHITE, ITEMS


class Backpack():
    def __init__(self):
        self.sizeX = 5
        self.sizeY = 5
        self.inventory = [[None for w in range(self.sizeX)] for h in range(self.sizeY)]
        self.toolbar = [None for x in range(self.sizeX)]


    def addInventory(self, item, x=None,y=None):
        if x and y:
            r = self.inventory[x][y]
            self.inventory[x][y] = item
            return r
        else:
            for vx in range(self.sizeX):
                for vy in range(self.sizeY):
                    if not self.inventory[vx][vy]:
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
        disp = pygame.surface.Surface((100,116))
        disp.fill(BLACK)
        empty = pygame.surface.Surface((16, 16))
        empty.fill(WHITE)
        x, y = 4, 4
        for i in self.inventory:
            for item in i:
                if item:
                    disp.blit(item.image, [x, y])
                else:
                    disp.blit(empty, [x, y])
                x += 16
            y += 16
            x = 4
        y += 8
        for item in self.toolbar:
            if item:
                disp.blit(item.image, [x, y])
            else:
                disp.blit(empty, [x, y])
            x += 16
        screen.blit(disp, [w/2-45, h/2-47])

    def __getitem__(self, item):
        for items in self.inventory:
            for i in items:
                if i and i.item == item:
                    return i

        for i in self.toolbar:
            if i and i.item == item:
                return i
        return None
