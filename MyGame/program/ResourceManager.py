# ResourceManager.py
import pygame

class ResourceManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ResourceManager, cls).__new__(cls)
            cls._instance.sprites = {}  # Önbellekte tutulan sprite'lar
            cls._instance.sounds = {}   # Önbellekte tutulan sesler
        return cls._instance
    
    def load_image(self, path, scale=None, convert_alpha=True):
        """Bir resmi yükler ve önbellekte tutar"""
        # Önbellekte kontrol et
        cache_key = f"{path}_{scale}"
        if cache_key in self.sprites:
            return self.sprites[cache_key]
        
        # Yükle ve ölçeklendir
        try:
            if convert_alpha:
                image = pygame.image.load(path).convert_alpha()
            else:
                image = pygame.image.load(path).convert()
                
            if scale:
                image = pygame.transform.scale(image, scale)
                
            # Önbelleğe ekle
            self.sprites[cache_key] = image
            return image
        except pygame.error as e:
            print(f"Resim yüklenirken hata: {path} - {e}")
            # Hata durumunda yedek bir görsel döndür
            placeholder = pygame.Surface(scale or (100, 100))
            placeholder.fill((255, 0, 255))  # Mor renk ile doldur (eksik texture göstergesi)
            return placeholder
    
    def load_animation_frames(self, base_path, prefix, count, scale=None):
        """Bir animasyon seti yükler ve döndürür"""
        frames = []
        for i in range(1, count + 1):
            img_path = f"{base_path}{prefix}{i}.png"
            frames.append(self.load_image(img_path, scale))
        return frames
    
    def preload_level_assets(self, level_name):
        """Bir level için gerekli tüm varlıkları önceden yükler"""
        # Level'a özgü asset listelerini tanımlayabilirsiniz
        pass