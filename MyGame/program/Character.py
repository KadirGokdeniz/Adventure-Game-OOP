# Character.py
from Entity import Entity
import json
import pygame

class Character(Entity):
    def __init__(self, level):
        # Temel sınıf başlatma
        super().__init__(0, 550, (200, 148), "others\\Character_images\\")
        
        self.level = level
        self.gold = 0
        
        # Level kontrolleri
        if level == 1:
            self.character_save_files()
        elif level == 2:
            self.character_load_files()
            self.y = 570
            
        if level != 0:
            self.gold = self.character_data["Gold"]
            self.hp = self.character_data["Hp"]
        
        # Karakter özel değişkenleri
        self.speed = 1.25
        self.action_mode = False
        self.animation = False
        self.is_attack1 = False
        self.is_attack2 = False
        self.is_jump = False
        
        # Düşman saldırı durumları
        self.is_attack11 = False
        self.is_attack12 = False
        self.is_attack13 = False
        self.is_attack21 = False
        self.is_attack22 = False
        self.is_attack23 = False
        
        # UI elemanları yükleme
        self.bMenu = self.resource_manager.load_image("others\\images\\bMenu.png", (400, 62))
        self.defeat = self.resource_manager.load_image("others\\images\\defeat.png", (400, 62))
        self.restart = self.resource_manager.load_image("others\\images\\restart.png",(500, 75))
        
        # Animasyonları yükleme
        self.load_animations()
    
    def load_animations(self):
        """Tüm animasyon setlerini yükler"""
        self.load_animation_set("breath", "b", 4, 250)
        self.load_animation_set("sword", "s", 4, 250)
        self.load_animation_set("run", "r", 6, 250)
        self.load_animation_set("draw_sword", "d", 4, 200)
        self.load_animation_set("back_sword", "d", 4, 200)  # Ters sıralamayı logic'te yapacağız
        self.load_animation_set("attack_mode1", "a1", 5, 150)
        self.load_animation_set("attack_mode2", "a2", 6, 300)
        self.load_animation_set("jump", "j", 4, 200)
        self.load_animation_set("fall", "f", 2, 200)
        self.load_animation_set("hurt", "h", 3, 150)
        self.load_animation_set("death", "dth", 6, 300)

    def character_save_files(self):
        """Karakter durumunu kaydeder"""
        self.character_data = {"Gold": self.gold, "Hp": self.hp}
        json.dump(self.character_data, open("others\\CharacterData.txt", "w"))

    def character_load_files(self):
        """Karakter durumunu yükler"""
        self.character_data = json.load(open("others\\CharacterData.txt", "r"))

    def Animation(self, Delay, animation_Number, limit_of_the_animation,condition=False,action_mode_end=False,status_mode_end="breath"):
        if pygame.time.get_ticks()-self.c_time>Delay:
            animation_Number+=1
            if self.c_status=="hurt" and animation_Number==1:
                if self.is_attack11:
                    self.c_hp-=1
                if self.is_attack12:
                    self.c_hp-=2
                if self.is_attack13:
                    self.c_hp-=3
                if self.is_attack21:
                    self.c_hp-=2
                if self.is_attack22:
                    self.c_hp-=4
                if self.is_attack23:
                    self.c_hp-=6
            if not(self.is_attack11 or self.is_attack12 or self.is_attack13 or self.is_attack21 or self.is_attack22 or self.is_attack23):
                self.is_attack11=False
                self.is_attack12=False
                self.is_attack13=False
                self._a=False
                self._a=False
                self._a=False
                
            if self.c_status=="attack_mode1" and animation_Number==2:
                self.c_is_attack1=True
            if self.c_status=="attack_mode2" and animation_Number==3:
                self.c_is_attack2=True
            if not((self.c_status=="attack_mode1" and animation_Number==2)or(self.c_status=="attack_mode2" and animation_Number==3)):
                self.c_is_attack1=False
                self.c_is_attack2=False
            if self.c_status=="fall":
                self.c_y+=60
            if self.c_status=="jump":
                self.c_y-=30
            if animation_Number== limit_of_the_animation and self.c_status!="death":
                animation_Number=0
                if condition:
                    self.c_action_mode=action_mode_end
                    self.c_status=status_mode_end
                    self.c_animation=False
            else:
                status_mode_end="death"
            self.c_time=pygame.time.get_ticks()
        return animation_Number

    def game_loop(self,key,mouse,is_victory,is_attack11,is_attack12,is_attack21,is_attack22,is_attack31,is_attack32):
        ##Action
        self.key=key
        self.mouse=mouse

        if is_attack11 and is_attack21 and is_attack31:
            self.is_attack13=True
        if (is_attack11 and is_attack21 and  not is_attack31)or (is_attack11 and not is_attack21 and is_attack31) or (not is_attack11 and is_attack21 and is_attack31):
            self.is_attack12=True
        if (is_attack11 and not is_attack21 and  not is_attack31)or (not is_attack11 and not is_attack21 and is_attack31) or (not is_attack11 and is_attack21 and not is_attack31):
            self.is_attack11=True
        if is_attack12 and is_attack22 and is_attack32:
            self._a=True
        if (is_attack12 and is_attack22 and  not is_attack32)or (is_attack12 and not is_attack22 and is_attack32) or (not is_attack12 and is_attack22 and is_attack32):
            self._a=True
        if (is_attack12 and not is_attack22 and  not is_attack32)or (not is_attack12 and not is_attack22 and is_attack32) or (not is_attack12 and is_attack22 and not is_attack32):
            self._a=True

        if self.key[pygame.K_d] and self.c_status!="death" and not is_victory :
            self.c_status="run"
            self.c_direction=False
            if self.c_x<1400 :
                self.c_x+=self.c_speed
            if self.c_x>=1400 and self.c_gold>80:
                self.c_x+=self.c_speed
        elif self.key[pygame.K_a] and self.c_status!="death"and not is_victory:
            self.c_status="run"
            self.c_direction=True
            if self.c_x>0 :
                self.c_x-=self.c_speed

        elif self.key[pygame.K_r] and self.c_status!="death"and not is_victory:
            if self.c_action_mode==False:
                self.c_status="draw_sword"
                self.c_animation=True
            elif self.c_action_mode==True:
                self.c_status="backsword"
                self.c_animation=True

        elif self.key[pygame.K_SPACE] and self.c_status!="death" and not is_victory:
            self.c_status="jump"
            self.c_animation=True

        elif self.mouse[2]==1 and self.c_status!="death" and not is_victory:
            self.c_status="attack_mode2"
            self.c_animation=True

        elif self.mouse[0]==1 and self.c_status!="death"and not is_victory :
            self.c_status="attack_mode1"
            self.c_animation=True

        elif self.c_status!="death"and not is_victory and (is_attack11 or is_attack12 or is_attack21 or is_attack22 or is_attack31 or is_attack32):
            self.c_status="hurt"
            if self.c_hp<=0:
                self.c_status="death"
            self.c_animation=True

        elif self.key[pygame.K_SPACE] and (self.c_status=="death" or is_victory):
            self.isRestart=True

        elif self.key[pygame.K_RETURN] and (self.c_status=="death" or is_victory):
            self.backMenu=True
        


        else:
            if self.c_animation==False:
                if self.c_action_mode==True:
                    self.c_status="sword"
                else:
                    self.c_status="breath"

        ##States
        if self.c_action_mode==False:
            if self.c_status=="breath":
                self.c_banimation=self.Animation(self.c_bdelay,self.c_banimation,4)
                
            elif self.c_status=="run":
                self.c_ranimation=self.Animation(self.c_rdelay,self.c_ranimation,6)
            
            elif self.c_status=="draw_sword":
                self.c_danimation=self.Animation(self.c_ddelay,self.c_danimation,4,self.c_animation,True,"sword")
            
            elif self.c_status=="attack_mode1":
                self.c_a1animation=self.Animation(self.c_a1delay,self.c_a1animation,5,self.c_animation,True,"sword")
            
            elif self.c_status=="attack_mode2":
                self.c_a2animation=self.Animation(self.c_a2delay,self.c_a2animation,6,self.c_animation,True,"sword")

            elif self.c_status=="fall":
                self.c_fanimation=self.Animation(self.c_fdelay,self.c_fanimation,2,self.c_animation,False,"sword")

            elif self.c_status=="jump":
                self.c_janimation=self.Animation(self.c_jdelay,self.c_janimation,5,self.c_animation,False,"sword")
                if self.c_janimation==4:
                    self.c_janimation=0
                    self.c_status="fall"

            elif self.c_status=="hurt":
                self.c_hanimation=self.Animation(self.c_hdelay,self.c_hanimation,3,self.c_animation,True,"breath")

            elif self.c_status=="death":
                self.c_dthanimation=self.Animation(self.c_dthdelay,self.c_dthanimation,6,self.c_animation,False,"sword")

        elif self.c_action_mode==True:
            if self.c_status=="sword":
                self.c_sanimation=self.Animation(self.c_sdelay,self.c_sanimation,4)
            
            elif self.c_status=="run":
                self.c_ranimation=self.Animation(self.c_rdelay,self.c_ranimation,6)
            
            elif self.c_status=="back_sword":
                self.c_danimation=self.Animation(self.c_ddelay,self.c_danimation,4,self.c_animation,False,"breath")
            
            elif self.c_status=="attack_mode1":
                self.c_a1animation=self.Animation(self.c_a1delay,self.c_a1animation,5,self.c_animation,True,"sword")
            
            elif self.c_status=="attack_mode2":
                self.c_a2animation=self.Animation(self.c_a2delay,self.c_a2animation,6,self.c_animation,True,"sword")
            
            elif self.c_status=="fall":
                self.c_fanimation=self.Animation(self.c_fdelay,self.c_fanimation,2,self.c_animation,True,"breath")
            
            elif self.c_status=="jump":
                self.c_janimation=self.Animation(self.c_jdelay,self.c_janimation,5,self.c_animation,True,"breath")
                if self.c_janimation==4:
                    self.c_janimation=0
                    self.c_status="fall"

            elif self.c_status=="hurt":
                self.c_hanimation=self.Animation(self.c_hdelay,self.c_hanimation,3,self.c_animation,True,"breath")

            elif self.c_status=="death":
                self.c_dthanimation=self.Animation(self.c_dthdelay,self.c_dthanimation,6,self.c_animation,False,"sword")
        
    def get_Rect(self):
        return pygame.Rect(self.c_x+65,self.c_y+30,55,120)