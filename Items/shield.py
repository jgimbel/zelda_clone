__author__ = 'joel'
from item import Item
class shield(Item):
    def __init__(self):
        super(pygame.sprite.Sprite,self).__init__("Sprites/items/shield.png")
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
