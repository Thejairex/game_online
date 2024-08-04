import pygame as pg

from const import Colors
from utils.create import Base

class Player(Base):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        return pg.draw.rect(screen, Colors.GREEN, self.rect)

    def action(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.move(-5, 0)
        if keys[pg.K_RIGHT]:
            self.move(5, 0)
        if keys[pg.K_UP]:
            self.move(0, -5)
        if keys[pg.K_DOWN]:
            self.move(0, 5)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy