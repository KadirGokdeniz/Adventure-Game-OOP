# Entity.py
import pygame

class Entity:
    def __init__(self, x, y, scale, path, hp=10):
        self.x = x
        self.y = y
        self.scale = scale
        self.path = path
        self.hp = hp
        
        self.status = "Breath"
        self.direction = False
        self.isDeath = False
        
        # Animasyon yönetimi
        self.animations = {}
        self.animation_counters = {}
        self.animation_delays = {}
        self.last_update = pygame.time.get_ticks()
        
    def load_animation_set(self, name, prefix, count, delay):
        """Bir animasyon seti yükler ve yapılandırır"""
        frames = []
        for i in range(1, count + 1):
            img_path = f"{self.path}{prefix}{i}.png"
            img = pygame.image.load(img_path).convert_alpha()
            frames.append(pygame.transform.scale(img, self.scale))
        
        self.animations[name] = frames
        self.animation_counters[name] = 0
        self.animation_delays[name] = delay
    
    def animate(self, name):
        """Animasyon karesini günceller ve indeksini döndürür"""
        if pygame.time.get_ticks() - self.last_update > self.animation_delays[name]:
            self.animation_counters[name] += 1
            if self.animation_counters[name] >= len(self.animations[name]):
                self.animation_counters[name] = 0
            self.last_update = pygame.time.get_ticks()
        return self.animation_counters[name]
    
    def draw(self, window):
        """Mevcut duruma göre varlığı çizer"""
        if self.status in self.animations:
            frame = self.animations[self.status][self.animation_counters[self.status]]
            window.blit(pygame.transform.flip(frame, self.direction, False), (self.x, self.y))
    
    def get_rect(self):
        """Çarpışma dikdörtgeni - alt sınıflarda özelleştirilmeli"""
        return pygame.Rect(self.x, self.y, self.scale[0], self.scale[1])