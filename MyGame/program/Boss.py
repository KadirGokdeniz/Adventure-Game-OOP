# Boss.py
from Entity import Entity
import pygame
from ResourceManager import ResourceManager

class Boss(Entity):
    def __init__(self, x):
        # Temel sınıf başlatma
        super().__init__(x, 400, (400, 300), "others\\Boss\\", hp=10)
        
        # ResourceManager örneği
        self.resource_manager = ResourceManager()
        
        # Boss özgü özellikler
        self.coins = [
            {"image": self.resource_manager.load_image("others\\images\\goldcoin.png", (40, 40)), 
             "pos": [self.x + 168, 607], 
             "collected": False},
            {"image": self.resource_manager.load_image("others\\images\\goldcoin.png", (40, 40)), 
             "pos": [self.x + 268, 607], 
             "collected": False},
            {"image": self.resource_manager.load_image("others\\images\\goldcoin.png", (40, 40)), 
             "pos": [self.x + 368, 607], 
             "collected": False}
        ]
        
        # Saldırı durumları
        self.is_attack1 = False
        self.is_attack2 = False
        
        # Boss özgü flag'ler
        self.action_mode = False
        self.animation = False
        self.is_death = False
        self.is_attack1 = False
        self.is_attack2 = False
        
        # Animasyonları yükle
        self.load_animations()
        
    def load_animations(self):
        """Tüm animasyon setlerini yükler"""
        self.load_animation_set("breath", "b", 6, 300)
        self.load_animation_set("run", "r", 6, 300)
        self.load_animation_set("attack_mode1", "a1", 8, 350)  # Boss daha güçlü olabilir
        self.load_animation_set("attack_mode2", "a2", 8, 350)
        self.load_animation_set("hurt", "h", 4, 150)
        self.load_animation_set("death", "d", 6, 400)  # Daha uzun ölüm animasyonu
        
    def draw(self, window, gold1collect=False, gold2collect=False, gold3collect=False):
        """Boss ve altınlarını çizer"""
        # Mevcut duruma göre çizim (demonAxe ile benzer ama daha karmaşık olabilir)
        if self.status == "breath":
            frame = self.animations["breath"][self.animation_counters["breath"]]
        elif self.status == "run":
            frame = self.animations["run"][self.animation_counters["run"]]
        elif self.status == "attack_mode1":
            frame = self.animations["attack_mode1"][self.animation_counters["attack_mode1"]]
        elif self.status == "attack_mode2":
            frame = self.animations["attack_mode2"][self.animation_counters["attack_mode2"]]
        elif self.status == "hurt":
            frame = self.animations["hurt"][self.animation_counters["hurt"]]
        elif self.status == "death":
            index = min(self.animation_counters["death"], len(self.animations["death"]) - 1)
            frame = self.animations["death"][index]
            
            # Ölüm durumunda altınları göster
            if self.is_death:
                if not gold1collect:
                    window.blit(self.coins[0]["image"], (self.coins[0]["pos"][0], self.coins[0]["pos"][1]))
                if not gold2collect:
                    window.blit(self.coins[1]["image"], (self.coins[1]["pos"][0], self.coins[1]["pos"][1]))
                if not gold3collect:
                    window.blit(self.coins[2]["image"], (self.coins[2]["pos"][0], self.coins[2]["pos"][1]))
                
        # Karakteri çiz
        window.blit(pygame.transform.flip(frame, self.direction, False), (self.x, self.y))
        
    def handle_movement(self, player_x):
        """Oyuncuya göre hareket mantığı - boss için daha karmaşık olabilir"""
        # Yön belirleme
        if player_x > self.x + 200 and not self.is_death:
            self.direction = False
        if player_x < self.x + 200 and not self.is_death:
            self.direction = True
            
        # Hareket mantığı (Boss daha stratejik hareket edebilir)
        if 0 < self.x - player_x <= 600 and not self.is_death:
            self.status = "run"
            self.animation = True
            self.action_mode = True
            self.x -= 0.5  # Boss daha yavaş hareket edebilir
        if 200 <= player_x - self.x <= 700 and not self.is_death:
            self.status = "run"
            self.animation = True
            self.action_mode = True
            self.x += 0.5
            
    def handle_attack(self, player_x, player_is_attack1, player_is_attack2):
        """Saldırı ve hasar mantığı - boss için daha karmaşık"""
        # Oyuncudan gelen saldırıları işle
        if player_is_attack1:
            self.is_attack1 = True
        if player_is_attack2:
            self.is_attack2 = True
            
        # Boss'un saldırı mesafesi daha uzun olabilir
        attack_distance = 200
        
        # Saldırı durumuna geç veya hasar al
        if self.direction == False and player_x - self.x <= attack_distance:
            if (player_is_attack1 or player_is_attack2) and not self.is_death:
                self.status = "hurt"
                if self.hp <= 0:
                    self.status = "death"
                    self.is_death = True
            if not (player_is_attack1 or player_is_attack2) and not self.is_death:
                # Boss'un farklı saldırı tipleri arasında rastgele seçim yap
                import random
                attack_type = random.choice(["attack_mode1", "attack_mode2"])
                self.status = attack_type
            self.animation = True
            
        if self.direction == True and player_x - self.x >= 0:
            if (player_is_attack1 or player_is_attack2) and not self.is_death:
                self.status = "hurt"
                if self.hp <= 0:
                    self.status = "death"
                    self.is_death = True
            if not (player_is_attack1 or player_is_attack2) and not self.is_death:
                import random
                attack_type = random.choice(["attack_mode1", "attack_mode2"])
                self.status = attack_type
            self.animation = True
            
    def update_animation_state(self):
        """Animasyon durumunu günceller"""
        # demonAxe ile benzer ancak boss'a özgü özellikler eklenebilir
        if self.action_mode:
            if self.status == "run":
                self.animation_counters["run"] = self.animate("run")
            elif self.status == "attack_mode1":
                self.animation_counters["attack_mode1"] = self.animate("attack_mode1")
                # Saldırı anı tespiti - boss için daha güçlü saldırılar
                if 3 <= self.animation_counters["attack_mode1"] <= 5:  # Uzun saldırı penceresi
                    self.is_attack1 = True
                else:
                    self.is_attack1 = False
            elif self.status == "attack_mode2":
                self.animation_counters["attack_mode2"] = self.animate("attack_mode2")
                # Saldırı anı tespiti
                if 3 <= self.animation_counters["attack_mode2"] <= 5:
                    self.is_attack2 = True
                else:
                    self.is_attack2 = False
            elif self.status == "breath":
                self.animation_counters["breath"] = self.animate("breath")
            elif self.status == "hurt":
                old_counter = self.animation_counters["hurt"]
                self.animation_counters["hurt"] = self.animate("hurt")
                # Hasar alma anı - boss daha dayanıklı olabilir
                if old_counter == 0 and self.animation_counters["hurt"] == 1:
                    if self.is_attack1:
                        self.hp -= 1  # Boss normal düşmandan daha az hasar alabilir
                    if self.is_attack2:
                        self.hp -= 1
                # Animasyon tamamlandı mı kontrol et
                if self.animation_counters["hurt"] == 0:
                    self.status = "breath"
                    self.animation = False
            elif self.status == "death":
                self.animation_counters["death"] = self.animate("death")
        else:
            if self.status == "breath":
                self.animation_counters["breath"] = self.animate("breath")
                
    def game_loop(self, player_x, player_is_attack1, player_is_attack2, player_status):
        """Ana oyun döngüsü - daha modüler yapıda"""
        # Hareket mantığı
        self.handle_movement(player_x)
        
        # Saldırı ve hasar mantığı
        self.handle_attack(player_x, player_is_attack1, player_is_attack2)
        
        # Animasyon güncelleme
        self.update_animation_state()
        
        # Altın pozisyonlarını güncelle (oyuncu hareket edebilir)
        self.update_coin_positions()
        
    def update_coin_positions(self):
        """Altın pozisyonlarını Boss pozisyonuna göre günceller"""
        if self.is_death:
            self.coins[0]["pos"][0] = self.x + 168
            self.coins[1]["pos"][0] = self.x + 268
            self.coins[2]["pos"][0] = self.x + 368
            
    def get_coin_rects(self):
        """Altınların çarpışma dikdörtgenlerini döndürür"""
        return [pygame.Rect(coin["pos"][0], coin["pos"][1], 30, 30) for coin in self.coins]