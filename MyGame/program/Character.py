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
        self.isAttack1 = False
        self.isAttack2 = False
        self.isJump = False
        
        # Düşman saldırı durumları
        self.isAttack11 = False
        self.isAttack12 = False
        self.isAttack13 = False
        self.isAttack21 = False
        self.isAttack22 = False
        self.isAttack23 = False
        
        # UI elemanları yükleme
        self.bMenu = pygame.image.load("others\\images\\bMenu.png").convert_alpha()
        self.bMenu = pygame.transform.scale(self.bMenu, (400, 62))
        self.defeat = pygame.image.load("others\\images\\defeat.png").convert_alpha()
        self.defeat = pygame.transform.scale(self.defeat, (400, 200))
        self.restart = pygame.image.load("others\\images\\restart.png").convert_alpha()
        self.restart = pygame.transform.scale(self.restart, (500, 75))
        
        # Animasyonları yükleme
        self.load_animations()
    
    def load_animations(self):
        """Tüm animasyon setlerini yükler"""
        self.load_animation_set("Breath", "b", 4, 250)
        self.load_animation_set("Sword", "s", 4, 250)
        self.load_animation_set("Run", "r", 6, 250)
        self.load_animation_set("DrawSword", "d", 4, 200)
        self.load_animation_set("BackSword", "d", 4, 200)  # Ters sıralamayı logic'te yapacağız
        self.load_animation_set("AttackMode1", "a1", 5, 150)
        self.load_animation_set("AttackMode2", "a2", 6, 300)
        self.load_animation_set("Jump", "j", 4, 200)
        self.load_animation_set("Fall", "f", 2, 200)
        self.load_animation_set("Hurt", "h", 3, 150)
        self.load_animation_set("Death", "dth", 6, 300)

    def character_save_files(self):
        """Karakter durumunu kaydeder"""
        self.character_data = {"Gold": self.gold, "Hp": self.hp}
        json.dump(self.character_data, open("others\\CharacterData.txt", "w"))

    def character_load_files(self):
        """Karakter durumunu yükler"""
        self.character_data = json.load(open("others\\CharacterData.txt", "r"))

    def Animation(self, Delay, animation_Number, limit_of_the_animation,condition=False,action_mode_end=False,status_mode_end="Breath"):
        if pygame.time.get_ticks()-self.c_time>Delay:
            animation_Number+=1
            if self.c_status=="Hurt" and animation_Number==1:
                if self.isAttack11:
                    self.c_hp-=1
                if self.isAttack12:
                    self.c_hp-=2
                if self.isAttack13:
                    self.c_hp-=3
                if self.isAttack21:
                    self.c_hp-=2
                if self.isAttack22:
                    self.c_hp-=4
                if self.isAttack23:
                    self.c_hp-=6
            if not(self.isAttack11 or self.isAttack12 or self.isAttack13 or self.isAttack21 or self.isAttack22 or self.isAttack23):
                self.isAttack11=False
                self.isAttack12=False
                self.isAttack13=False
                self.isAttack21=False
                self.isAttack22=False
                self.isAttack23=False
                
            if self.c_status=="AttackMode1" and animation_Number==2:
                self.c_isAttack1=True
            if self.c_status=="AttackMode2" and animation_Number==3:
                self.c_isAttack2=True
            if not((self.c_status=="AttackMode1" and animation_Number==2)or(self.c_status=="AttackMode2" and animation_Number==3)):
                self.c_isAttack1=False
                self.c_isAttack2=False
            if self.c_status=="Fall":
                self.c_y+=60
            if self.c_status=="Jump":
                self.c_y-=30
            if animation_Number== limit_of_the_animation and self.c_status!="Death":
                animation_Number=0
                if condition:
                    self.c_action_mode=action_mode_end
                    self.c_status=status_mode_end
                    self.c_animation=False
            else:
                status_mode_end="Death"
            self.c_time=pygame.time.get_ticks()
        return animation_Number

    def GameLoop(self,key,mouse,isVictory,isAttack11,isAttack12,isAttack21,isAttack22,isAttack31,isAttack32):
        ##Action
        self.key=key
        self.mouse=mouse

        if isAttack11 and isAttack21 and isAttack31:
            self.isAttack13=True
        if (isAttack11 and isAttack21 and  not isAttack31)or (isAttack11 and not isAttack21 and isAttack31) or (not isAttack11 and isAttack21 and isAttack31):
            self.isAttack12=True
        if (isAttack11 and not isAttack21 and  not isAttack31)or (not isAttack11 and not isAttack21 and isAttack31) or (not isAttack11 and isAttack21 and not isAttack31):
            self.isAttack11=True
        if isAttack12 and isAttack22 and isAttack32:
            self.isAttack23=True
        if (isAttack12 and isAttack22 and  not isAttack32)or (isAttack12 and not isAttack22 and isAttack32) or (not isAttack12 and isAttack22 and isAttack32):
            self.isAttack22=True
        if (isAttack12 and not isAttack22 and  not isAttack32)or (not isAttack12 and not isAttack22 and isAttack32) or (not isAttack12 and isAttack22 and not isAttack32):
            self.isAttack21=True

        if self.key[pygame.K_d] and self.c_status!="Death" and not isVictory :
            self.c_status="Run"
            self.c_direction=False
            if self.c_x<1400 :
                self.c_x+=self.c_speed
            if self.c_x>=1400 and self.c_gold>80:
                self.c_x+=self.c_speed
        elif self.key[pygame.K_a] and self.c_status!="Death"and not isVictory:
            self.c_status="Run"
            self.c_direction=True
            if self.c_x>0 :
                self.c_x-=self.c_speed

        elif self.key[pygame.K_r] and self.c_status!="Death"and not isVictory:
            if self.c_action_mode==False:
                self.c_status="DrawSword"
                self.c_animation=True
            elif self.c_action_mode==True:
                self.c_status="BackSword"
                self.c_animation=True

        elif self.key[pygame.K_SPACE] and self.c_status!="Death" and not isVictory:
            self.c_status="Jump"
            self.c_animation=True

        elif self.mouse[2]==1 and self.c_status!="Death" and not isVictory:
            self.c_status="AttackMode2"
            self.c_animation=True

        elif self.mouse[0]==1 and self.c_status!="Death"and not isVictory :
            self.c_status="AttackMode1"
            self.c_animation=True

        elif self.c_status!="Death"and not isVictory and (isAttack11 or isAttack12 or isAttack21 or isAttack22 or isAttack31 or isAttack32):
            self.c_status="Hurt"
            if self.c_hp<=0:
                self.c_status="Death"
            self.c_animation=True

        elif self.key[pygame.K_SPACE] and (self.c_status=="Death" or isVictory):
            self.isRestart=True

        elif self.key[pygame.K_RETURN] and (self.c_status=="Death" or isVictory):
            self.backMenu=True
        


        else:
            if self.c_animation==False:
                if self.c_action_mode==True:
                    self.c_status="Sword"
                else:
                    self.c_status="Breath"

        ##States
        if self.c_action_mode==False:
            if self.c_status=="Breath":
                self.c_banimation=self.Animation(self.c_bdelay,self.c_banimation,4)
                
            elif self.c_status=="Run":
                self.c_ranimation=self.Animation(self.c_rdelay,self.c_ranimation,6)
            
            elif self.c_status=="DrawSword":
                self.c_danimation=self.Animation(self.c_ddelay,self.c_danimation,4,self.c_animation,True,"Sword")
            
            elif self.c_status=="AttackMode1":
                self.c_a1animation=self.Animation(self.c_a1delay,self.c_a1animation,5,self.c_animation,True,"Sword")
            
            elif self.c_status=="AttackMode2":
                self.c_a2animation=self.Animation(self.c_a2delay,self.c_a2animation,6,self.c_animation,True,"Sword")

            elif self.c_status=="Fall":
                self.c_fanimation=self.Animation(self.c_fdelay,self.c_fanimation,2,self.c_animation,False,"Sword")

            elif self.c_status=="Jump":
                self.c_janimation=self.Animation(self.c_jdelay,self.c_janimation,5,self.c_animation,False,"Sword")
                if self.c_janimation==4:
                    self.c_janimation=0
                    self.c_status="Fall"

            elif self.c_status=="Hurt":
                self.c_hanimation=self.Animation(self.c_hdelay,self.c_hanimation,3,self.c_animation,True,"Breath")

            elif self.c_status=="Death":
                self.c_dthanimation=self.Animation(self.c_dthdelay,self.c_dthanimation,6,self.c_animation,False,"Sword")

        elif self.c_action_mode==True:
            if self.c_status=="Sword":
                self.c_sanimation=self.Animation(self.c_sdelay,self.c_sanimation,4)
            
            elif self.c_status=="Run":
                self.c_ranimation=self.Animation(self.c_rdelay,self.c_ranimation,6)
            
            elif self.c_status=="BackSword":
                self.c_danimation=self.Animation(self.c_ddelay,self.c_danimation,4,self.c_animation,False,"Breath")
            
            elif self.c_status=="AttackMode1":
                self.c_a1animation=self.Animation(self.c_a1delay,self.c_a1animation,5,self.c_animation,True,"Sword")
            
            elif self.c_status=="AttackMode2":
                self.c_a2animation=self.Animation(self.c_a2delay,self.c_a2animation,6,self.c_animation,True,"Sword")
            
            elif self.c_status=="Fall":
                self.c_fanimation=self.Animation(self.c_fdelay,self.c_fanimation,2,self.c_animation,True,"Breath")
            
            elif self.c_status=="Jump":
                self.c_janimation=self.Animation(self.c_jdelay,self.c_janimation,5,self.c_animation,True,"Breath")
                if self.c_janimation==4:
                    self.c_janimation=0
                    self.c_status="Fall"


            elif self.c_status=="Hurt":
                self.c_hanimation=self.Animation(self.c_hdelay,self.c_hanimation,3,self.c_animation,True,"Breath")

            elif self.c_status=="Death":
                self.c_dthanimation=self.Animation(self.c_dthdelay,self.c_dthanimation,6,self.c_animation,False,"Sword")
        
    def get_Rect(self):
        return pygame.Rect(self.c_x+65,self.c_y+30,55,120)