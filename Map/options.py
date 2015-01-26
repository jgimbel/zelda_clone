__author__ = 'joel'
from resources import INVFONT
class Option:

    hovered = False
    def __init__(self, screen, text, pos, function):
        self.text = text
        self.pos = pos
        self.screen = screen
        self.set_rect()
        self.draw()
        self.function = function

    def draw(self):
        self.set_rend()
        self.screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = INVFONT.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos