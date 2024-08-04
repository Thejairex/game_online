import pygame as pg


class Base:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, screen, color):
        return pg.draw.rect(screen, color, self.rect)

class Structure(Base):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def hitbox(self, entity):
        pass
        