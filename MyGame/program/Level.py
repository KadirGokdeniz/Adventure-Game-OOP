# Level.py
from abc import ABC, abstractmethod
import pygame
from ResourceManager import ResourceManager

class Level(ABC):
    """
    Tüm level sınıfları için temel abstract class.
    Bu sınıf, tüm level'ların uygulaması gereken ortak arayüzü tanımlar.
    """
    def __init__(self, width, height, resource_manager=None):
        """
        Level sınıfı için temel constructor.
        
        Args:
            width: Pencere genişliği
            height: Pencere yüksekliği  
            resource_manager: ResourceManager örneği veya None (None ise yeni oluşturulur)
        """
        self.width = width
        self.height = height
        self.resource_manager = resource_manager or ResourceManager()
        
        # Level özel başlatma
        self.initialize()
    
    @abstractmethod
    def initialize(self):
        """
        Level-specific initialization after base initialization.
        Her alt sınıf kendi özel başlatma kodunu burada tanımlamalıdır.
        """
        pass
    
    @abstractmethod
    def draw(self, window):
        """
        Level içeriğini belirtilen pencereye çizer.
        
        Args:
            window: pygame Surface nesnesi
        """
        pass
    
    @abstractmethod
    def game_loop(self, key, mouse):
        """
        Level'ın oyun mantığını işler.
        
        Args:
            key: Pygame key state
            mouse: Pygame mouse state
            
        Returns:
            str or None: Eğer level değişikliği gerekiyorsa sonraki level adı,
                         aksi halde None
        """
        pass