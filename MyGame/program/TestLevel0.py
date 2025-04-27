# TestLevel0.py
from Level import Level
import pygame

class TestLevel0(Level):
    """Ana menüyü temsil eden level."""
    
    def initialize(self):
        """Level özel başlatma işlemleri"""
        # ESKİ __init__ içeriğini buraya taşıyın, aşağıdakiler gibi
        self.background = self.resource_manager.load_image(
            "others\\TestLevels0\\background0.png", 
            (self.width, self.height)
        )
        self.start = self.resource_manager.load_image(
            "others\\images\\start.png", 
            (600, 80)
        )
        self.controllers = self.resource_manager.load_image(
            "others\\images\\controllers.png", 
            (600, 80)
        )
    
    def draw(self, window):
        """Level içeriğini pencereye çiz"""
        window.blit(self.background, (0, 0))
        window.blit(self.start, (500, 300))
        window.blit(self.controllers, (500, 500))
    
    def game_loop(self, key, mouse):
        """Oyun mantığını işle"""
        self.key = key
        self.mouse = mouse
        
        if self.key[pygame.K_SPACE]:
            return "Options"
        elif self.key[pygame.K_RETURN]:
            return "Test Level1"
            
        return None  # Level değişimi yoksa None döndür