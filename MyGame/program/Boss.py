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
        self.isAttack1 = False
        self.isAttack2 = False
        
        # Boss özgü flag'ler
        self.action_mode = False
        self.animation = False
        self.isDeath = False
        self.isAttack1 = False
        self.isAttack2 = False
        
        # Animasyonları yükle
        self.load_animations()
        
    def load_animations(self):
        """Tüm animasyon setlerini yükler"""
        self.load_animation_set("Breath", "b", 6, 300)
        self.load_animation_set("Run", "r", 6, 300)
        self.load_animation_set("AttackMode1", "a1", 8, 350)  # Boss daha güçlü olabilir
        self.load_animation_set("AttackMode2", "a2", 8, 350)
        self.load_animation_set("Hurt", "h", 4, 150)
        self.load_animation_set("Death", "d", 6, 400)  # Daha uzun ölüm animasyonu
        
    def draw(self, window, gold1collect=False, gold2collect=False, gold3collect=False):
        """Boss ve altınlarını çizer"""
        # Mevcut duruma göre çizim (demonAxe ile benzer ama daha karmaşık olabilir)
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
            index = min(self.animation_counters["Death"], len(self.animations["Death"]) - 1)
            frame = self.animations["Death"][index]
            
            # Ölüm durumunda altınları göster
            if self.isDeath:
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
        if player_x > self.x + 200 and not self.isDeath:
            self.direction = False
        if player_x < self.x + 200 and not self.isDeath:
            self.direction = True
            
        # Hareket mantığı (Boss daha stratejik hareket edebilir)
        if 0 < self.x - player_x <= 600 and not self.isDeath:
            self.status = "Run"
            self.animation = True
            self.action_mode = True
            self.x -= 0.5  # Boss daha yavaş hareket edebilir
        if 200 <= player_x - self.x <= 700 and not self.isDeath:
            self.status = "Run"
            self.animation = True
            self.action_mode = True
            self.x += 0.5
            
    def handle_attack(self, player_x, player_is_attack1, player_is_attack2):
        """Saldırı ve hasar mantığı - boss için daha karmaşık"""
        # Oyuncudan gelen saldırıları işle
        if player_is_attack1:
            self.isAttack1 = True
        if player_is_attack2:
            self.isAttack2 = True
            
        # Boss'un saldırı mesafesi daha uzun olabilir
        attack_distance = 200
        
        # Saldırı durumuna geç veya hasar al
        if self.direction == False and player_x - self.x <= attack_distance:
            if (player_is_attack1 or player_is_attack2) and not self.isDeath:
                self.status = "Hurt"
                if self.hp <= 0:
                    self.status = "Death"
                    self.isDeath = True
            if not (player_is_attack1 or player_is_attack2) and not self.isDeath:
                # Boss'un farklı saldırı tipleri arasında rastgele seçim yap
                import random
                attack_type = random.choice(["AttackMode1", "AttackMode2"])
                self.status = attack_type
            self.animation = True
            
        if self.direction == True and player_x - self.x >= 0:
            if (player_is_attack1 or player_is_attack2) and not self.isDeath:
                self.status = "Hurt"
                if self.hp <= 0:
                    self.status = "Death"
                    self.isDeath = True
            if not (player_is_attack1 or player_is_attack2) and not self.isDeath:
                import random
                attack_type = random.choice(["AttackMode1", "AttackMode2"])
                self.status = attack_type
            self.animation = True
            
    def update_animation_state(self):
        """Animasyon durumunu günceller"""
        # demonAxe ile benzer ancak boss'a özgü özellikler eklenebilir
        if self.action_mode:
            if self.status == "Run":
                self.animation_counters["Run"] = self.animate("Run")
            elif self.status == "AttackMode1":
                self.animation_counters["AttackMode1"] = self.animate("AttackMode1")
                # Saldırı anı tespiti - boss için daha güçlü saldırılar
                if 3 <= self.animation_counters["AttackMode1"] <= 5:  # Uzun saldırı penceresi
                    self.isAttack1 = True
                else:
                    self.isAttack1 = False
            elif self.status == "AttackMode2":
                self.animation_counters["AttackMode2"] = self.animate("AttackMode2")
                # Saldırı anı tespiti
                if 3 <= self.animation_counters["AttackMode2"] <= 5:
                    self.isAttack2 = True
                else:
                    self.isAttack2 = False
            elif self.status == "Breath":
                self.animation_counters["Breath"] = self.animate("Breath")
            elif self.status == "Hurt":
                old_counter = self.animation_counters["Hurt"]
                self.animation_counters["Hurt"] = self.animate("Hurt")
                # Hasar alma anı - boss daha dayanıklı olabilir
                if old_counter == 0 and self.animation_counters["Hurt"] == 1:
                    if self.isAttack1:
                        self.hp -= 1  # Boss normal düşmandan daha az hasar alabilir
                    if self.isAttack2:
                        self.hp -= 1
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
        
        # Altın pozisyonlarını güncelle (oyuncu hareket edebilir)
        self.update_coin_positions()
        
    def update_coin_positions(self):
        """Altın pozisyonlarını Boss pozisyonuna göre günceller"""
        if self.isDeath:
            self.coins[0]["pos"][0] = self.x + 168
            self.coins[1]["pos"][0] = self.x + 268
            self.coins[2]["pos"][0] = self.x + 368
            
    def get_coin_rects(self):
        """Altınların çarpışma dikdörtgenlerini döndürür"""
        return [pygame.Rect(coin["pos"][0], coin["pos"][1], 30, 30) for coin in self.coins]