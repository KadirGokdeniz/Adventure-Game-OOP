import pygame
from Character import Character
from demonAxe import demonAxe

class TestLevel1:
    def __init__(self,windows_width,windows_height):
        self.background=pygame.image.load("others\\TestLevels1\\background1.jpg").convert_alpha()
        self.background=pygame.transform.scale(self.background,(windows_width,windows_height))
        self.Character=Character(1)
        self.demonAxe1=demonAxe(1000)
        self.demonAxe2=demonAxe(0)
        self.demonAxe3=demonAxe(100)
        self.demonAxe4=demonAxe(1200)
        self.demonAxe5=demonAxe(1100)
        self.demonAxe6=demonAxe(1000)
        self.isVictory=False
        
        self.gold1collect=False
        self.gold2collect=False
        self.gold3collect=False
        self.gold4collect=False
        self.gold5collect=False
        self.gold6collect=False

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
    
    def Draw(self,window):
        window.blit(self.background,(0,0))
        if self.Character.c_hp==10:
            window.blit(self.hp10,(40,30))
        if self.Character.c_hp==9:
            window.blit(self.hp9,(40,30))
        if self.Character.c_hp==8:
            window.blit(self.hp8,(40,30))
        if self.Character.c_hp==7:
            window.blit(self.hp7,(40,30))
        if self.Character.c_hp==6:
            window.blit(self.hp6,(40,30))
        if self.Character.c_hp==5:
            window.blit(self.hp5,(40,30))
        if self.Character.c_hp==4:
            window.blit(self.hp4,(40,30))
        if self.Character.c_hp==3:
            window.blit(self.hp3,(40,30))
        if self.Character.c_hp==2:
            window.blit(self.hp2,(40,30))
        if self.Character.c_hp==1:
            window.blit(self.hp1,(40,30))
        if self.Character.c_hp<=0:
            window.blit(self.hp0,(40,30))
        
        window.blit(self.gold,(1300,40))
        window.blit(self._0,(1430,45))
        tens=int((self.Character.c_gold%100)/10)
        hundres=int((self.Character.c_gold-tens*10)/100)
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

        self.Character.Draw(window)
        if not self.gold1collect:
            self.demonAxe1.Draw(window)
        if self.demonAxe1.d_isDeath==True:
            if not self.gold2collect:
                self.demonAxe2.Draw(window)
            if not self.gold3collect:
                self.demonAxe3.Draw(window)
            if self.demonAxe2.d_isDeath==True and self.demonAxe3.d_isDeath==True:
                if not self.gold4collect:
                    self.demonAxe4.Draw(window)
                if not self.gold5collect:
                    self.demonAxe5.Draw(window)
                if not self.gold6collect:
                    self.demonAxe6.Draw(window)

    def GameLoop(self,key,mouse):
        self.key=key
        if (self.Character.get_Rect()).colliderect(self.demonAxe1.d_x+158,607,30,30) and self.demonAxe1.d_isDeath==True and self.gold1collect==False:
            self.Character.c_gold+=10
            self.gold1collect=True
        
        if (self.Character.get_Rect()).colliderect(self.demonAxe2.d_x+158,607,30,30) and self.demonAxe2.d_isDeath==True and self.gold2collect==False:
            self.Character.c_gold+=10
            self.gold2collect=True
        
        if (self.Character.get_Rect()).colliderect(self.demonAxe3.d_x+158,607,30,30) and self.demonAxe3.d_isDeath==True and self.gold3collect==False:
            self.Character.c_gold+=10
            self.gold3collect=True
        
        if (self.Character.get_Rect()).colliderect(self.demonAxe4.d_x+158,607,30,30) and self.demonAxe4.d_isDeath==True and self.gold4collect==False:
            self.Character.c_gold+=10
            self.gold4collect=True
        
        if (self.Character.get_Rect()).colliderect(self.demonAxe5.d_x+158,607,30,30) and self.demonAxe5.d_isDeath==True and self.gold5collect==False:
            self.Character.c_gold+=10
            self.gold5collect=True
        
        if (self.Character.get_Rect()).colliderect(self.demonAxe6.d_x+158,607,30,30) and self.demonAxe6.d_isDeath==True and self.gold6collect==False:
            self.Character.c_gold+=10
            self.gold6collect=True
        
        if self.demonAxe1.d_isDeath==False:
            self.Character.GameLoop(key,mouse,self.isVictory,self.demonAxe1.d_isAttack1,self.demonAxe1.d_isAttack2,False,False,False,False)
        self.demonAxe1.GameLoop(self.Character.c_x,self.Character.c_isAttack1,self.Character.c_isAttack2,self.Character.c_status)
        if self.demonAxe1.d_isDeath==True:
            if self.demonAxe2.d_isDeath==False and self.demonAxe3.d_isDeath==False:
                self.Character.GameLoop(key,mouse,self.isVictory,self.demonAxe2.d_isAttack1,self.demonAxe2.d_isAttack2,self.demonAxe3.d_isAttack1,self.demonAxe3.d_isAttack2,False,False)
            if self.demonAxe2.d_isDeath==False and self.demonAxe3.d_isDeath==True:
                self.Character.GameLoop(key,mouse,self.isVictory,self.demonAxe2.d_isAttack1,self.demonAxe2.d_isAttack2,False,False,False,False)
            if self.demonAxe2.d_isDeath==True and self.demonAxe3.d_isDeath==False:
                self.Character.GameLoop(key,mouse,self.isVictory,False,False,self.demonAxe3.d_isAttack1,self.demonAxe3.d_isAttack2,False,False)
            self.demonAxe2.GameLoop(self.Character.c_x,self.Character.c_isAttack1,self.Character.c_isAttack2,self.Character.c_status)
            self.demonAxe3.GameLoop(self.Character.c_x,self.Character.c_isAttack1,self.Character.c_isAttack2,self.Character.c_status)
            if self.demonAxe2.d_isDeath==True and self.demonAxe3.d_isDeath==True:
                if self.demonAxe4.d_isDeath==False and self.demonAxe5.d_isDeath==False and self.demonAxe6.d_isDeath==False:
                    self.Character.GameLoop(key,mouse,self.isVictory,self.demonAxe4.d_isAttack1,self.demonAxe4.d_isAttack2,self.demonAxe5.d_isAttack1,self.demonAxe5.d_isAttack2,self.demonAxe6.d_isAttack1,self.demonAxe6.d_isAttack2)
                elif self.demonAxe4.d_isDeath==False and self.demonAxe5.d_isDeath==False and self.demonAxe6.d_isDeath==True:
                    self.Character.GameLoop(key,mouse,self.isVictory,self.demonAxe4.d_isAttack1,self.demonAxe4.d_isAttack2,self.demonAxe5.d_isAttack1,self.demonAxe5.d_isAttack2,False,False)
                elif self.demonAxe4.d_isDeath==False and self.demonAxe5.d_isDeath==True and self.demonAxe6.d_isDeath==False:
                    self.Character.GameLoop(key,mouse,self.isVictory,self.demonAxe4.d_isAttack1,self.demonAxe4.d_isAttack2,False,False,self.demonAxe6.d_isAttack1,self.demonAxe6.d_isAttack2)
                elif self.demonAxe4.d_isDeath==True and self.demonAxe5.d_isDeath==False and self.demonAxe6.d_isDeath==False:
                    self.Character.GameLoop(key,mouse,self.isVictory,False,False,self.demonAxe5.d_isAttack1,self.demonAxe5.d_isAttack2,self.demonAxe6.d_isAttack1,self.demonAxe6.d_isAttack2)
                elif self.demonAxe4.d_isDeath==False and self.demonAxe5.d_isDeath==True and self.demonAxe6.d_isDeath==True:
                    self.Character.GameLoop(key,mouse,self.isVictory,self.demonAxe4.d_isAttack1,self.demonAxe4.d_isAttack2,False,False,False,False)
                elif self.demonAxe4.d_isDeath==True and self.demonAxe5.d_isDeath==False and self.demonAxe6.d_isDeath==True:
                    self.Character.GameLoop(key,mouse,self.isVictory,False,False,self.demonAxe5.d_isAttack1,self.demonAxe5.d_isAttack2,False,False)
                elif self.demonAxe4.d_isDeath==True and self.demonAxe5.d_isDeath==True and self.demonAxe6.d_isDeath==False:
                    self.Character.GameLoop(key,mouse,self.isVictory,False,False,False,False,self.demonAxe6.d_isAttack1,self.demonAxe6.d_isAttack2)
                elif self.demonAxe4.d_isDeath==True and self.demonAxe5.d_isDeath==True and self.demonAxe6.d_isDeath==True:
                    self.Character.GameLoop(key,mouse,self.isVictory,False,False,False,False,False,False)
                self.demonAxe4.GameLoop(self.Character.c_x,self.Character.c_isAttack1,self.Character.c_isAttack2,self.Character.c_status)
                self.demonAxe5.GameLoop(self.Character.c_x,self.Character.c_isAttack1,self.Character.c_isAttack2,self.Character.c_status)
                self.demonAxe6.GameLoop(self.Character.c_x,self.Character.c_isAttack1,self.Character.c_isAttack2,self.Character.c_status)
        if  self.Character.c_x>=1400 and self.Character.c_gold>=60:
            self.Character.Character_Save_Files()
            return "Test Level2"
        
        elif self.key[pygame.K_SPACE] and self.Character.c_status=="Death":
            return "Test Level1"
        
        elif self.key[pygame.K_TAB] and self.Character.c_status=="Death":
            return "Test Level0"