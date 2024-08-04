import pygame as pg

from const import Colors
from player import Player
from utils.create import Structure

class Game:
    def __init__(self):
        pg.display.set_caption("Game")
        
        self.screen = pg.display.set_mode((640, 480))
        self.playing = True
    
        self.player = Player(100, 100, 50, 50)
        self.table = Structure(300, 200, 100, 50)

        self.fps = 120
        self.clock = pg.time.Clock()
        
        
        
    def run(self):
        while self.playing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False
            
            
            
            self.screen.fill(Colors.BLACK)
            
            
            self.player.action()
            
            self.table.draw(self.screen, Colors.SKY)
            self.player.draw(self.screen)
            self.table.hitbox(self.player)
        
            pg.display.flip()

            self.clock.tick(self.fps)
if __name__ == "__main__":
    game = Game()
    game.run()