# TestLevel1.py
from Level import Level
import pygame
from Character import Character
from demonAxe import DemonAxe
from ResourceManager import ResourceManager as resource_manager
class TestLevel1:
    """Birinci oyun seviyesi"""
    
    def initialize(self):
        """Level özel başlatma işlemleri"""
        # ESKİ __init__ içeriğindeki kodlar
        self.background = pygame.image.load("others\\TestLevels1\\background1.jpg").convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        # Character ve DemonAxe örnekleri
        self.character = Character(1)  # Level 1 karakteri
        self.demon_axe1 = DemonAxe(1000)
        self.demon_axe2 = DemonAxe(0)
        self.demon_axe3 = DemonAxe(100)
        self.demon_axe4 = DemonAxe(1200)
        self.demon_axe5 = DemonAxe(1100)
        self.demon_axe6 = DemonAxe(1000)

        self.is_victory=False
        self.gold1_collect=False
        self.gold2_collect=False
        self.gold3_collect=False
        self.gold4_collect=False
        self.gold5_collect=False
        self.gold6_collect=False

        self.path1="others\\images\\"

        self.hp10 = self.resource_manager.load_image(self.path1+"h10.jpg",(200,50))

        self.hp9 = self.resource_manager.load_image(self.path1+"h9.jpg",(200,50))

        self.hp8 = self.resource_manager.load_image(self.path1+"h8.jpg",(200,50))

        self.hp7 = self.resource_manager.load_image(self.path1+"h7.jpg",(200,50))

        self.hp6 = self.resource_manager.load_image(self.path1+"h6.jpg",(200,50))

        self.hp5 = self.resource_manager.load_image(self.path1+"h5.jpg",(200,50))

        self.hp4 = self.resource_manager.load_image(self.path1+"h4.jpg",(200,50))

        self.hp3 = self.resource_manager.load_image(self.path1+"h3.jpg",(200,50))

        self.hp2 = self.resource_manager.load_image(self.path1+"h2.jpg",(200,50))

        self.hp1 = self.resource_manager.load_image(self.path1+"h1.jpg",(200,50))

        self.hp0 = self.resource_manager.load_image(self.path1+"h0.jpg",(200,50))

        self._0 = self.resource_manager.load_image(self.path1+"0.jpg",(200,50))

        self._1 = self.resource_manager.load_image(self.path1+"1.jpg",(200,50))

        self._2 = self.resource_manager.load_image(self.path1+"2.jpg",(200,50))

        self._3 = self.resource_manager.load_image(self.path1+"3.jpg",(200,50))

        self._4 = self.resource_manager.load_image(self.path1+"4.jpg",(200,50))

        self._5 = self.resource_manager.load_image(self.path1+"5.jpg",(200,50))

        self._6 = self.resource_manager.load_image(self.path1+"6.jpg",(200,50))

        self._7 = self.resource_manager.load_image(self.path1+"7.jpg",(200,50))

        self._8 = self.resource_manager.load_image(self.path1+"0.jpg",(200,50))

        self._9 = self.resource_manager.load_image(self.path1+"9.jpg",(200,50))

        self.gold = self.resource_manager.load_image(self.path1+"gold.jpg",(60,35))
    
    def draw(self,window):
        """Level içeriğini pencereye çiz"""
        # ESKİ Draw metodu içeriği
        window.blit(self.background, (0, 0))

        if self.character.c_hp==10:
            window.blit(self.hp10,(40,30))
        if self.character.c_hp==9:
            window.blit(self.hp9,(40,30))
        if self.character.c_hp==8:
            window.blit(self.hp8,(40,30))
        if self.character.c_hp==7:
            window.blit(self.hp7,(40,30))
        if self.character.c_hp==6:
            window.blit(self.hp6,(40,30))
        if self.character.c_hp==5:
            window.blit(self.hp5,(40,30))
        if self.character.c_hp==4:
            window.blit(self.hp4,(40,30))
        if self.character.c_hp==3:
            window.blit(self.hp3,(40,30))
        if self.character.c_hp==2:
            window.blit(self.hp2,(40,30))
        if self.character.c_hp==1:
            window.blit(self.hp1,(40,30))
        if self.character.c_hp<=0:
            window.blit(self.hp0,(40,30))
        
        window.blit(self.gold,(1300,40))
        window.blit(self._0,(1430,45))

        tens=int((self.character.c_gold%100)/10)
        hundres=int((self.character.c_gold-tens*10)/100)

        if tens==0:
            window.blit(self._0,(1400,45))
        if tens==1:
            window.blit(self._1,(1400,45))
        if tens==2:
            window.blit(self._2,(1400,45))
        if tens==3:
            window.blit(self._3,(1400,45))
        if tens==4:
            window.blit(self._4,(1400,45))
        if tens==5:
            window.blit(self._5,(1400,45))
        if tens==6:
            window.blit(self._6,(1400,45))
        if tens==7:
            window.blit(self._7,(1400,45))
        if tens==8:
            window.blit(self._8,(1400,45))
        if tens==9:
            window.blit(self._9,(1400,45))

        if hundres==0:
            window.blit(self._0,(1370,45))
        if hundres==1:
            window.blit(self._1,(1370,45))
        if hundres==2:
            window.blit(self._2,(1370,45))
        if hundres==3:
            window.blit(self._3,(1370,45))
        if hundres==4:
            window.blit(self._4,(1370,45))
        if hundres==5:
            window.blit(self._5,(1370,45))
        if hundres==6:
            window.blit(self._6,(1370,45))
        if hundres==7:
            window.blit(self._7,(1370,45))
        if hundres==8:
            window.blit(self._8,(1370,45))
        if hundres==9:
            window.blit(self._9,(1370,45))

        # Karakter ve düşmanları çiz
        self.character.draw(window)
        if not self.gold1_collect:
            self.demon_axe1.draw(window)
        # ... diğer çizim mantığı
        if self.demon_axe1.is_death==True:
            if not self.gold2_collect:
                self.demon_axe2.draw(window)
            if not self.gold3_collect:
                self.demon_axe3.draw(window)
            if self.demon_axe2.is_death==True and self.demon_axe3._==True:
                if not self.gold4_collect:
                    self.demon_axe4.draw(window)
                if not self.gold5_collect:
                    self.demon_axe5.draw(window)
                if not self.gold6_collect:
                    self.demon_axe6.draw(window)

    def game_loop(self,key,mouse):
        """Oyun mantığını işle"""
        self.key=key

        if (self.character.get_Rect()).colliderect(self.demon_axe1.d_x+158,607,30,30) and self.demon_axe1.is_death==True and self.gold1_collect==False:
            self.character.c_gold+=10
            self.gold1_collect=True
        
        if (self.character.get_Rect()).colliderect(self.demon_axe2.d_x+158,607,30,30) and self.demon_axe2.is_death==True and self.gold2_collect==False:
            self.character.c_gold+=10
            self.gold2_collect=True
        
        if (self.character.get_Rect()).colliderect(self.demon_axe3.d_x+158,607,30,30) and self.demon_axe3.is_death==True and self._==False:
            self.character.c_gold+=10
            self.gold3_collect=True
        
        if (self.character.get_Rect()).colliderect(self.demon_axe4.d_x+158,607,30,30) and self.demon_axe4.is_death==True and self._==False:
            self.character.c_gold+=10
            self.gold4_collect=True
        
        if (self.character.get_Rect()).colliderect(self.demon_axe5.d_x+158,607,30,30) and self.demon_axe5.is_death==True and self._==False:
            self.character.c_gold+=10
            self.gold5_collect=True
        
        if (self.character.get_Rect()).colliderect(self.demon_axe6.d_x+158,607,30,30) and self.demon_axe6.is_death==True and self._==False:
            self.character.c_gold+=10
            self.gold6_collect=True
        
        if self.demon_axe1.is_death==False:
            self.character.game_loop(key,mouse,self.is_victory,self.demon_axe1.is_attack1,self.demon_axe1.is_attack2,False,False,False,False)
        self.demon_axe1.game_loop(self.character.c_x,self.character.c_is_attack1,self.character.is_attack2,self.character.c_status)
        if self.demon_axe1.is_death==True:
            if self.demon_axe2.is_death==False and self.demon_axe3.is_death==False:
                self.character.game_loop(key,mouse,self.is_victory,self.demon_axe2.is_attack1,self.demon_axe2.is_attack2,self.demon_axe3.is_attack1,self.demon_axe3.is_attack2,False,False)
            if self.demon_axe2.is_death==False and self.demon_axe3.is_death==True:
                self.character.game_loop(key,mouse,self.is_victory,self.demon_axe2.is_attack1,self.demon_axe2.is_attack2,False,False,False,False)
            if self.demon_axe2.is_death==True and self.demon_axe3.is_death==False:
                self.character.game_loop(key,mouse,self.is_victory,False,False,self.demon_axe3.is_attack1,self.demon_axe3.is_attack2,False,False)
            self.demon_axe2.game_loop(self.character.c_x,self.character.c_is_attack1,self.character.c_is_attack2,self.character.c_status)
            self.demon_axe3.game_loop(self.character.c_x,self.character.c_is_attack1,self.character.c_is_attack2,self.character.c_status)
            if self.demon_axe2.is_death==True and self.demon_axe3.is_death==True:
                if self.demon_axe4.is_death==False and self.demon_axe5.is_death==False and self.demon_axe6.is_death==False:
                    self.character.game_loop(key,mouse,self.is_victory,self.demon_axe4.is_attack1,self.demon_axe4.is_attack2,self.demon_axe5.is_attack1,self.demon_axe5.is_attack2,self.demon_axe6.is_attack1,self.demon_axe6.is_attack2)
                elif self.demon_axe4.is_death==False and self.demon_axe5.is_death==False and self.demon_axe6.is_death==True:
                    self.character.game_loop(key,mouse,self.is_victory,self.demon_axe4.is_attack1,self.demon_axe4.is_attack2,self.demon_axe5.is_attack1,self.demon_axe5.is_attack2,False,False)
                elif self.demon_axe4.is_death==False and self.demon_axe5.is_death==True and self.demon_axe6.is_death==False:
                    self.character.game_loop(key,mouse,self.is_victory,self.demon_axe4.is_attack1,self.demon_axe4.is_attack2,False,False,self.demon_axe6.is_attack1,self.demon_axe6.is_attack2)
                elif self.demon_axe4.is_death==True and self.demon_axe5.is_death==False and self.demon_axe6.is_death==False:
                    self.character.game_loop(key,mouse,self.is_victory,False,False,self.demon_axe5.is_attack1,self.demon_axe5.is_attack2,self.demon_axe6.is_attack1,self.demon_axe6.is_attack2)
                elif self.demon_axe4.is_death==False and self.demon_axe5.is_death==True and self.demon_axe6.is_death==True:
                    self.character.game_loop(key,mouse,self.is_victory,self.demon_axe4.is_attack1,self.demon_axe4.is_attack2,False,False,False,False)
                elif self.demon_axe4.is_death==True and self.demon_axe5.is_death==False and self.demon_axe6.is_death==True:
                    self.character.game_loop(key,mouse,self.is_victory,False,False,self.demon_axe5.is_attack1,self.demon_axe5.is_attack2,False,False)
                elif self.demon_axe4.is_death==True and self.demon_axe5.is_death==True and self.demon_axe6.is_death==False:
                    self.character.game_loop(key,mouse,self.is_victory,False,False,False,False,self.demon_axe6.is_attack1,self.demon_axe6.is_attack2)
                elif self.demon_axe4.is_death==True and self.demon_axe5.is_death==True and self.demon_axe6.is_death==True:
                    self.character.game_loop(key,mouse,self.is_victory,False,False,False,False,False,False)
                self.demon_axe4.game_loop(self.character.c_x,self.character.c_is_attack1,self.character.c_is_attack2,self.character.c_status)
                self.demon_axe5.game_loop(self.character.c_x,self.character.c_is_attack1,self.character.c_is_attack2,self.character.c_status)
                self.demon_axe6.game_loop(self.character.c_x,self.character.c_is_attack1,self.character.c_is_attack2,self.character.c_status)
        if  self.character.c_x>=1400 and self.character.c_gold>=60:
            self.character.character_save_files()
            return "Test Level2"
        
        elif self.key[pygame.K_SPACE] and self.character.c_status=="Death":
            return "Test Level1"
        
        elif self.key[pygame.K_TAB] and self.character.c_status=="Death":
            return "Test Level0"