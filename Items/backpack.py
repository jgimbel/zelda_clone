__author__ = 'joel'
import pygame

from resources import BLACK, WHITE, INVFONT


class Backpack():
    def __init__(self):
        self.sizeX = 5
        self.sizeY = 5
        self.inventory = [[Slot(None) for w in range(self.sizeX)] for h in range(self.sizeY)]
        self.toolbar = [Slot(None) for x in range(self.sizeX)]

    def addInventory(self, item, x=None,y=None):
        if x is not None and y is not None:
            if self.inventory[x].type == item.type:
                self.inventory[x].add(item)
                return None
            else:
                r = self.inventory[x][y]
                self.inventory[x][y] = item
                return r
        else:
            for vx in range(self.sizeX):
                for vy in range(self.sizeY):
                    if self.inventory[vx].type == item.type:
                        self.inventory[vx].add(item)
                        return None

            for vx in range(self.sizeX):
                for vy in range(self.sizeY):
                    if self.inventory[vx].type is None:
                        r = self.inventory[vx]
                        self.inventory[vx].setType(item)
                        self.inventory[vx].add(item)
                        return r

    def addToolbar(self, item, x=None):
        if x:
            if self.toolbar[x].type == item.type:
                self.toolbar[x].add(item)
                return None
            else:
                r = self.toolbar[x]
                self.toolbar[x] = item
                return r
        else:
            for vx in range(self.sizeX):
                if self.toolbar[vx].type == item.type:
                    print self.toolbar[vx]
                    self.toolbar[vx].add(item)
                    return None
            for vx in range(self.sizeX):
                if self.toolbar[vx].type is None:
                    r = self.toolbar[vx]
                    self.toolbar[vx].setType(item)
                    self.toolbar[vx].add(item)
                    return r
            return self.addInventory(item)

    def drop(self, item):
        for i in self.toolbar:
            if i.type == item:
                t = i.sprites()[0]
                i.remove(t)
                return t

        for items in self.inventory:
            for i in items:
                if i.type == item:
                    t = i.sprites()[0]
                    i.remove(t)
                    return t

    def draw(self, screen):
        w, h = screen.get_size()
        disp = pygame.surface.Surface((176,220))
        disp.fill(BLACK)
        empty = pygame.surface.Surface((32, 32))
        empty.fill(WHITE)
        x, y = 4, 4
        for i in self.inventory:
            for item in i:
                if item.type:
                    disp.blit(item.image, [x, y])
                    disp.blit(INVFONT.render(str(len(item)), True, WHITE, BLACK), [x+16, y+16])
                else:
                    disp.blit(empty, [x, y])
                x += 34
            y += 34
            x = 4
        y += 8
        for item in self.toolbar:
            if item:
                disp.blit(item.image, [x, y])
                disp.blit(INVFONT.render(str(len(item)), True, WHITE, BLACK), [x+16, y+16])
            else:
                disp.blit(empty, [x, y])
            x += 32
        screen.blit(disp, [w/2-176/2, h/2-220/2])

    def __getitem__(self, item):
        for i in self.toolbar:
            if i.type == item and len(i.sprites()) > 0:
                return i.sprites()[0]

        for items in self.inventory:
            for i in items and len(i.sprites()) > 0:
                if i.type == item:
                    return i.sprites()[0]

        return None

class Slot(pygame.sprite.Group):
    def __init__(self, item):
        super(Slot, self).__init__()
        if item:
            self.image = item.image
            self.type = item.type
        else:
            self.image = None
            self.type = None

    def setType(self, item):
        self.image = item.image
        self.type = item.type

    def __str__(self):
        r = super(Slot, self).__str__()
        r += ", " + str(self.type)
        return r