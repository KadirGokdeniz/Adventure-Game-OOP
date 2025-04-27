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
        self.isAttack1 = False
        self.isAttack2 = False
        
        # demonAxe özgü flag'ler
        self.action_mode = False
        self.animation = False
        self.isDeath = False
        self.isAttack1 = False
        self.isAttack2 = False
        
        # Animasyonları yükle
        self.load_animations()
        
    def load_animations(self):
        """Tüm animasyon setlerini yükler"""
        self.load_animation_set("Breath", "b", 6, 250)
        self.load_animation_set("Run", "r", 6, 250)
        self.load_animation_set("AttackMode1", "a1", 6, 300)
        self.load_animation_set("AttackMode2", "a2", 6, 300)
        self.load_animation_set("Hurt", "h", 3, 100)
        self.load_animation_set("Death", "d", 4, 300)
        
    def draw(self, window):
        """demonAxe ve altınını çizer"""
        # Mevcut duruma göre çizim
        if self.status == "Breath":
            frame = self.animations["Breath"][self.animation_counters["Breath"]]
        elif self.status == "Run":
            frame = self.animations["Run"][self.animation_counters["Run"]]
        elif self.status == "AttackMode1":
            frame = self.animations["AttackMode1"][self.animation_counters["AttackMode1"]]
        elif self.status == "AttackMode2":
            frame = self.animations["AttackMode2"][self.animation_counters["AttackMode2"]]
        elif self.status == "Hurt":
            frame = self.animations["Hurt"][self.animation_counters["Hurt"]]
        elif self.status == "Death":
            if self.animation_counters["Death"] >= 3:
                frame = self.animations["Death"][3]  # Son kare
                # Altını göster
                window.blit(self.coin, (self.coin_pos[0], self.coin_pos[1]))
            else:
                frame = self.animations["Death"][self.animation_counters["Death"]]
                
        # Karakteri çiz
        window.blit(pygame.transform.flip(frame, self.direction, False), (self.x, self.y))
        
    def handle_movement(self, player_x):
        """Oyuncuya göre hareket mantığı"""
        # Yön belirleme
        if player_x - 31 > self.x and not self.isDeath:
            self.direction = False
            self.coin_pos[0] = self.x + 150
        if player_x - 31 < self.x and not self.isDeath:
            self.direction = True
            self.coin_pos[0] = self.x + 150
            
        # Hareket mantığı
        if 0 < self.x - player_x <= 500 and not self.isDeath:
            self.status = "Run"
            self.animation = True
            self.action_mode = True
            self.x -= 0.75
        if 150 <= player_x - self.x <= 662 and not self.isDeath:
            self.status = "Run"
            self.animation = True
            self.action_mode = True
            self.x += 0.75
            
    def handle_attack(self, player_x, player_is_attack1, player_is_attack2):
        """Saldırı ve hasar mantığı"""
        # Oyuncudan gelen saldırıları işle
        if player_is_attack1:
            self.isAttack1 = True
        if player_is_attack2:
            self.isAttack2 = True
            
        # Saldırı durumuna geç veya hasar al
        if self.direction == False and player_x - self.x <= 150:
            if (player_is_attack1 or player_is_attack2) and not self.isDeath:
                self.status = "Hurt"
                if self.hp <= 0:
                    self.status = "Death"
                    self.isDeath = True
            if not (player_is_attack1 or player_is_attack2) and not self.isDeath:
                self.status = "AttackMode1"
            self.animation = True
            
        if self.direction == True and player_x - self.x >= 0:
            if (player_is_attack1 or player_is_attack2) and not self.isDeath:
                self.status = "Hurt"
                if self.hp <= 0:
                    self.status = "Death"
                    self.isDeath = True
            if not (player_is_attack1 or player_is_attack2) and not self.isDeath:
                self.status = "AttackMode1"
            self.animation = True
            
    def update_animation_state(self):
        """Animasyon durumunu günceller"""
        if self.action_mode:
            if self.status == "Run":
                self.animation_counters["Run"] = self.animate("Run")
            elif self.status == "AttackMode1":
                self.animation_counters["AttackMode1"] = self.animate("AttackMode1")
                # Saldırı anı tespiti
                if self.animation_counters["AttackMode1"] == 3:
                    self.isAttack1 = True
                else:
                    self.isAttack1 = False
            elif self.status == "AttackMode2":
                self.animation_counters["AttackMode2"] = self.animate("AttackMode2")
                # Saldırı anı tespiti
                if self.animation_counters["AttackMode2"] == 3:
                    self.isAttack2 = True
                else:
                    self.isAttack2 = False
            elif self.status == "Breath":
                self.animation_counters["Breath"] = self.animate("Breath")
            elif self.status == "Hurt":
                old_counter = self.animation_counters["Hurt"]
                self.animation_counters["Hurt"] = self.animate("Hurt")
                # Hasar alma anı (animasyonun ilk karesi değiştiğinde)
                if old_counter == 0 and self.animation_counters["Hurt"] == 1:
                    if self.isAttack1:
                        self.hp -= 1
                    if self.isAttack2:
                        self.hp -= 2
                # Animasyon tamamlandı mı kontrol et
                if self.animation_counters["Hurt"] == 0:
                    self.status = "Breath"
                    self.animation = False
            elif self.status == "Death":
                self.animation_counters["Death"] = self.animate("Death")
        else:
            if self.status == "Breath":
                self.animation_counters["Breath"] = self.animate("Breath")
                
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