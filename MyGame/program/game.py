import pygame 
import sys
sys.path.append("/")
from TestLevel1 import TestLevel1
from TestLevel2 import TestLevel2
from TestLevel0 import TestLevel0
from Options import Options

pygame.init()

class Game:
    def __init__(self):
        self.height=800
        self.width=1550
        self.window=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("My Game")
        
        self.level_lock="Test Level0"
        self.UpdateLevel()
        self.clock=pygame.time.Clock()

    def UpdateLevel(self):
        if self.level_lock=="Test Level0":
             self.current_level=TestLevel0(self.width,self.height)
        elif self.level_lock=="Options":
            self.current_level=Options(self.width,self.height)
        elif self.level_lock=="Test Level1":
            self.current_level=TestLevel1(self.width,self.height)
        elif self.level_lock=="Test Level2":
            self.current_level=TestLevel2(self.width,self.height)
        self.level_lock=None

    def draw(self):
        self.current_level.Draw(self.window)
        pygame.display.update()

    def game_loop(self):     
        self.key=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return "QUIT"
        self.Mouse=pygame.mouse.get_pressed()
        self.level_lock=self.current_level.GameLoop(self.key,self.Mouse)
        if self.level_lock!=None:
            self.UpdateLevel()
        self.draw()

game=Game()
while True:
    game_status= game.game_loop()
    if game_status is not None:
        break