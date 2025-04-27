# demonAxe.py
from Entity import Entity
import pygame
from ResourceManager import ResourceManager

class DemonAxe(Entity):
    def __init__(self, x):
        # Temel sınıf başlatma
        super().__init__(x, 440, (375, 277.5), "others\\DemonAxe\\", hp=3)
        
        # ResourceManager örneği
        self.resource_manager = ResourceManager()
        
        # demonAxe özgü özellikler
        self.coin = self.resource_manager.load_image("others\\images\\goldcoin.png", (40, 40))
        self.coin_pos = [self.x - 100, 600]
        self.coin_rect = pygame.Rect(self.coin_pos[0], self.coin_pos[1] + 15, 25, 25)
        
        # Saldırı durumları
        self.is_attack1 = False
        self.is_attack2 = False
        
        # demonAxe özgü flag'ler
        self.action_mode = False
        self.animation = False
        self.is_death = False
        self.is_attack1 = False
        self.is_attack2 = False
        
        # Animasyonları yükle
        self.load_animations()
        
    def load_animations(self):
        """Tüm animasyon setlerini yükler"""
        self.load_animation_set("breath", "b", 6, 250)
        self.load_animation_set("run", "r", 6, 250)
        self.load_animation_set("attack_mode1", "a1", 6, 300)
        self.load_animation_set("attack_mode2", "a2", 6, 300)
        self.load_animation_set("hurt", "h", 3, 100)
        self.load_animation_set("death", "d", 4, 300)
        
    def draw(self, window):
        """demonAxe ve altınını çizer"""
        # Mevcut duruma göre çizim
        if self.status == "breath":
            frame = self.animations["breath"][self.animation_counters["breath"]]
        elif self.status == "r":
            frame = self.animations["r"][self.animation_counters["r"]]
        elif self.status == "attack_mode1":
            frame = self.animations["attack_mode1"][self.animation_counters["attack_mode1"]]
        elif self.status == "attack_mode2":
            frame = self.animations["attack_mode2"][self.animation_counters["attack_mode2"]]
        elif self.status == "hurt":
            frame = self.animations["hurt"][self.animation_counters["hurt"]]
        elif self.status == "death":
            if self.animation_counters["death"] >= 3:
                frame = self.animations["death"][3]  # Son kare
                # Altını göster
                window.blit(self.coin, (self.coin_pos[0], self.coin_pos[1]))
            else:
                frame = self.animations["death"][self.animation_counters["death"]]
                
        # Karakteri çiz
        window.blit(pygame.transform.flip(frame, self.direction, False), (self.x, self.y))
        
    def handle_movement(self, player_x):
        """Oyuncuya göre hareket mantığı"""
        # Yön belirleme
        if player_x - 31 > self.x and not self.is_death:
            self.direction = False
            self.coin_pos[0] = self.x + 150
        if player_x - 31 < self.x and not self.is_death:
            self.direction = True
            self.coin_pos[0] = self.x + 150
            
        # Hareket mantığı
        if 0 < self.x - player_x <= 500 and not self.is_death:
            self.status = "r"
            self.animation = True
            self.action_mode = True
            self.x -= 0.75
        if 150 <= player_x - self.x <= 662 and not self.is_death:
            self.status = "r"
            self.animation = True
            self.action_mode = True
            self.x += 0.75
            
    def handle_attack(self, player_x, player_is_attack1, player_is_attack2):
        """Saldırı ve hasar mantığı"""
        # Oyuncudan gelen saldırıları işle
        if player_is_attack1:
            self.is_attack1 = True
        if player_is_attack2:
            self.is_attack2 = True
            
        # Saldırı durumuna geç veya hasar al
        if self.direction == False and player_x - self.x <= 150:
            if (player_is_attack1 or player_is_attack2) and not self.is_death:
                self.status = "hurt"
                if self.hp <= 0:
                    self.status = "death"
                    self.is_death = True
            if not (player_is_attack1 or player_is_attack2) and not self.is_death:
                self.status = "attack_mode1"
            self.animation = True
            
        if self.direction == True and player_x - self.x >= 0:
            if (player_is_attack1 or player_is_attack2) and not self.is_death:
                self.status = "hurt"
                if self.hp <= 0:
                    self.status = "death"
                    self.is_death = True
            if not (player_is_attack1 or player_is_attack2) and not self.is_death:
                self.status = "attack_mode1"
            self.animation = True
            
    def update_animation_state(self):
        """Animasyon durumunu günceller"""
        if self.action_mode:
            if self.status == "r":
                self.animation_counters["r"] = self.animate("r")
            elif self.status == "attack_mode1":
                self.animation_counters["attack_mode1"] = self.animate("attack_mode1")
                # Saldırı anı tespiti
                if self.animation_counters["attack_mode1"] == 3:
                    self.is_attack1 = True
                else:
                    self.is_attack1 = False
            elif self.status == "attack_mode2":
                self.animation_counters["attack_mode2"] = self.animate("attack_mode2")
                # Saldırı anı tespiti
                if self.animation_counters["attack_mode2"] == 3:
                    self.is_attack2 = True
                else:
                    self.is_attack2 = False
            elif self.status == "breath":
                self.animation_counters["breath"] = self.animate("breath")
            elif self.status == "hurt":
                old_counter = self.animation_counters["hurt"]
                self.animation_counters["hurt"] = self.animate("hurt")
                # Hasar alma anı (animasyonun ilk karesi değiştiğinde)
                if old_counter == 0 and self.animation_counters["hurt"] == 1:
                    if self.is_attack1:
                        self.hp -= 1
                    if self.is_attack2:
                        self.hp -= 2
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
        
        # Coin pozisyonunu güncelle
        self.coin_rect = pygame.Rect(self.coin_pos[0], self.coin_pos[1] + 15, 25, 25)