import pygame
from Character import Character
from Boss   import Boss

class TestLevel2:
    def __init__(self,windows_width,windows_height):
        self.background=pygame.image.load("others\\TestLevels2\\background2.png").convert_alpha()
        self.background=pygame.transform.scale(self.background,(windows_width,windows_height))
        self.Character=Character(2)

        self.Boss=Boss(1100)
        self.isVictory=False
        self.path2="others\\images\\"

        self.gold1collect=False
        self.gold2collect=False
        self.gold3collect=False

        self.victory=pygame.image.load(self.path2+"victory.png").convert_alpha()
        self.victory=pygame.transform.scale(self.victory,(400,200))

        self.hp10=pygame.image.load(self.path2+"h10.jpg").convert_alpha()
        self.hp10=pygame.transform.scale(self.hp10,(200,50))

        self.hp9=pygame.image.load(self.path2+"h9.jpg").convert_alpha()
        self.hp9=pygame.transform.scale(self.hp9,(200,50))

        self.hp8=pygame.image.load(self.path2+"h8.jpg").convert_alpha()
        self.hp8=pygame.transform.scale(self.hp8,(200,50))

        self.hp7=pygame.image.load(self.path2+"h7.jpg").convert_alpha()
        self.hp7=pygame.transform.scale(self.hp7,(200,50))

        self.hp6=pygame.image.load(self.path2+"h6.jpg").convert_alpha()
        self.hp6=pygame.transform.scale(self.hp6,(200,50))

        self.hp5=pygame.image.load(self.path2+"h5.jpg").convert_alpha()
        self.hp5=pygame.transform.scale(self.hp5,(200,50))

        self.hp4=pygame.image.load(self.path2+"h4.jpg").convert_alpha()
        self.hp4=pygame.transform.scale(self.hp4,(200,50))

        self.hp3=pygame.image.load(self.path2+"h3.jpg").convert_alpha()
        self.hp3=pygame.transform.scale(self.hp3,(200,50))

        self.hp2=pygame.image.load(self.path2+"h2.jpg").convert_alpha()
        self.hp2=pygame.transform.scale(self.hp2,(200,50))

        self.hp1=pygame.image.load(self.path2+"h1.jpg").convert_alpha()
        self.hp1=pygame.transform.scale(self.hp1,(200,50))

        self.hp0=pygame.image.load(self.path2+"h0.jpg").convert_alpha()
        self.hp0=pygame.transform.scale(self.hp0,(200,50))

        self.hpb10=pygame.image.load(self.path2+"hb10.jpg").convert_alpha()
        self.hpb10=pygame.transform.scale(self.hpb10,(250,50))

        self.hpb9=pygame.image.load(self.path2+"hb9.jpg").convert_alpha()
        self.hpb9=pygame.transform.scale(self.hpb9,(250,50))

        self.hpb8=pygame.image.load(self.path2+"hb8.jpg").convert_alpha()
        self.hpb8=pygame.transform.scale(self.hpb8,(250,50))

        self.hpb7=pygame.image.load(self.path2+"hb7.jpg").convert_alpha()
        self.hpb7=pygame.transform.scale(self.hpb7,(250,50))

        self.hpb6=pygame.image.load(self.path2+"hb6.jpg").convert_alpha()
        self.hpb6=pygame.transform.scale(self.hpb6,(250,50))

        self.hpb5=pygame.image.load(self.path2+"hb5.jpg").convert_alpha()
        self.hpb5=pygame.transform.scale(self.hpb5,(250,50))

        self.hpb4=pygame.image.load(self.path2+"hb4.jpg").convert_alpha()
        self.hpb4=pygame.transform.scale(self.hpb4,(250,50))

        self.hpb3=pygame.image.load(self.path2+"hb3.jpg").convert_alpha()
        self.hpb3=pygame.transform.scale(self.hpb3,(250,50))

        self.hpb2=pygame.image.load(self.path2+"hb2.jpg").convert_alpha()
        self.hpb2=pygame.transform.scale(self.hpb2,(250,50))

        self.hpb1=pygame.image.load(self.path2+"hb1.jpg").convert_alpha()
        self.hpb1=pygame.transform.scale(self.hpb1,(250,50))

        self.hpb0=pygame.image.load(self.path2+"hb0.jpg").convert_alpha()
        self.hpb0=pygame.transform.scale(self.hpb0,(250,50))

        self._0=pygame.image.load(self.path2+"0.png").convert_alpha()
        self._0=pygame.transform.scale(self._0,(20,30))

        self._1=pygame.image.load(self.path2+"1.png").convert_alpha()
        self._1=pygame.transform.scale(self._1,(20,30))

        self._2=pygame.image.load(self.path2+"2.png").convert_alpha()
        self._2=pygame.transform.scale(self._2,(20,30))

        self._3=pygame.image.load(self.path2+"3.png").convert_alpha()
        self._3=pygame.transform.scale(self._3,(20,30))

        self._4=pygame.image.load(self.path2+"4.png").convert_alpha()
        self._4=pygame.transform.scale(self._4,(20,30))

        self._5=pygame.image.load(self.path2+"5.png").convert_alpha()
        self._5=pygame.transform.scale(self._5,(20,30))

        self._6=pygame.image.load(self.path2+"6.png").convert_alpha()
        self._6=pygame.transform.scale(self._6,(20,30))

        self._7=pygame.image.load(self.path2+"7.png").convert_alpha()
        self._7=pygame.transform.scale(self._7,(20,30))

        self._8=pygame.image.load(self.path2+"8.png").convert_alpha()
        self._8=pygame.transform.scale(self._8,(20,30))

        self._9=pygame.image.load(self.path2+"9.png").convert_alpha()
        self._9=pygame.transform.scale(self._9,(20,30))

        self.gold=pygame.image.load(self.path2+"gold.png").convert_alpha()
        self.gold=pygame.transform.scale(self.gold,(60,30))
    
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
        tens=(self.Character.c_gold%100)/10
        hundres=(self.Character.c_gold-tens*10)/100
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

        if self.Boss.b_hp==10:
            window.blit(self.hpb10,(1250,730))
        if self.Boss.b_hp==9:
            window.blit(self.hpb9,(1250,730))
        if self.Boss.b_hp==8:
            window.blit(self.hpb8,(1250,730))
        if self.Boss.b_hp==7:
            window.blit(self.hpb7,(1250,730))
        if self.Boss.b_hp==6:
            window.blit(self.hpb6,(1250,730))
        if self.Boss.b_hp==5:
            window.blit(self.hpb5,(1250,730))
        if self.Boss.b_hp==4:
            window.blit(self.hpb4,(1250,730))
        if self.Boss.b_hp==3:
            window.blit(self.hpb3,(1250,730))
        if self.Boss.b_hp==2:
            window.blit(self.hpb2,(1250,730))
        if self.Boss.b_hp==1:
            window.blit(self.hpb1,(1250,730))
        if self.Boss.b_hp<=0:
            window.blit(self.hpb0,(1250,730))

        self.Character.Draw(window)
        if self.Character.c_x>=1400 and self.Character.c_gold>=90:
            self.Character.Character_Save_Files()
            window.blit(self.victory,(550,266))
            self.isVictory=True
            window.blit(self.Character.bMenu,(540,600))
            window.blit(self.Character.restart,(500,500))
        self.Boss.Draw(window,self.gold1collect,self.gold2collect,self.gold3collect)
            
    def GameLoop(self,key,mouse):
        self.key=key
        self.Character.GameLoop(key,mouse,self.isVictory,self.Boss.b_isAttack1,self.Boss.b_isAttack2,False,False,False,False)
        self.Boss.GameLoop(self.Character.c_x,self.Character.c_isAttack1,self.Character.c_isAttack2,self.Character.c_status)
        if (self.Character.get_Rect()).colliderect(self.Boss.b_x+168,607,30,30) and self.Boss.b_isDeath==True and self.gold1collect==False:
            self.Character.c_gold+=10
            self.gold1collect=True
        
        if (self.Character.get_Rect()).colliderect(self.Boss.b_x+268,607,30,30) and self.Boss.b_isDeath==True and self.gold2collect==False:
            self.Character.c_gold+=10
            self.gold2collect=True
        
        if (self.Character.get_Rect()).colliderect(self.Boss.b_x+368,607,30,30) and self.Boss.b_isDeath==True and self.gold3collect==False:
            self.Character.c_gold+=10
            self.gold3collect=True
        
        elif self.key[pygame.K_SPACE] and (self.Character.c_status=="Death" or self.isVictory):
            return "Test Level1"
        
        elif self.key[pygame.K_TAB] and (self.Character.c_status=="Death" or self.isVictory):
            return "Test Level0"