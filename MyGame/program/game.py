# Game.py
import pygame
import sys
sys.path.append("/")

from TestLevel0 import TestLevel0
from TestLevel1 import TestLevel1
from TestLevel2 import TestLevel2
from Options import Options
from ResourceManager import ResourceManager

class Game:
    def __init__(self):
        self.height = 800
        self.width = 1550
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")
        
        # Merkezi ResourceManager oluştur
        self.resource_manager = ResourceManager()
        
        self.level_lock = "Test Level0"
        self.update_level()
        self.clock = pygame.time.Clock()
    
    def update_level(self):
        """Level değişikliği gerçekleştiğinde çağrılır"""
        # Level factory pattern
        level_factory = {
            "Test Level0": lambda: TestLevel0(self.width, self.height, self.resource_manager),
            "Options": lambda: Options(self.width, self.height, self.resource_manager),
            "Test Level1": lambda: TestLevel1(self.width, self.height, self.resource_manager),
            "Test Level2": lambda: TestLevel2(self.width, self.height, self.resource_manager)
        }
        
        if self.level_lock in level_factory:
            self.current_level = level_factory[self.level_lock]()
        
        self.level_lock = None
    
    def draw(self):
        """Aktif level'ı çiz"""
        self.current_level.draw(self.window)
        pygame.display.update()
    
    def game_loop(self):
        """Ana oyun döngüsü"""
        self.key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
                
        self.mouse = pygame.mouse.get_pressed()
        self.level_lock = self.current_level.game_loop(self.key, self.mouse)
        
        if self.level_lock is not None:
            self.update_level()
            
        self.draw()