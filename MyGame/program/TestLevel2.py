import pygame
from Character import Character
from Boss   import Boss

class TestLevel2:
    def __init__(self,windows_width,windows_height):
        self.background=pygame.image.load("others\\TestLevels2\\background2.png").convert_alpha()
        self.background=pygame.transform.scale(self.background,(windows_width,windows_height))
        self.character=Character(2)

        self.Boss=Boss(1100)
        self.is_victory=False
        self.path2="others\\images\\"

        self.gold1_collect=False
        self.gold2_collect=False
        self.gold3_collect=False

        self.victory=pygame.image.load(self.path2+"victory.png").convert_alpha()
        self.victory=pygame.transform.scale(self.victory,(400,200))

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

        self.hpb10 = self.resource_manager.load_image(self.path1+"hb10.jpg",(200,50))

        self.hpb9 = self.resource_manager.load_image(self.path1+"hb9.jpg",(200,50))

        self.hpb8 = self.resource_manager.load_image(self.path1+"hb8.jpg",(200,50))

        self.hpb7 = self.resource_manager.load_image(self.path1+"hb7.jpg",(200,50))

        self.hpb6 = self.resource_manager.load_image(self.path1+"hb6.jpg",(200,50))

        self.hpb5 = self.resource_manager.load_image(self.path1+"hb5.jpg",(200,50))

        self.hpb4 = self.resource_manager.load_image(self.path1+"hb4.jpg",(200,50))

        self.hpb3 = self.resource_manager.load_image(self.path1+"hb3.jpg",(200,50))

        self.hpb2 = self.resource_manager.load_image(self.path1+"hb2.jpg",(200,50))

        self.hpb1 = self.resource_manager.load_image(self.path1+"hb1.jpg",(200,50))

        self.hpb0 = self.resource_manager.load_image(self.path1+"hb0.jpg",(200,50))

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
        window.blit(self.background,(0,0))
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
        tens=(self.character.c_gold%100)/10
        hundres=(self.character.c_gold-tens*10)/100
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

        self.character.draw(window)
        if self.character.c_x>=1400 and self.character.c_gold>=90:
            self.character.character_save_files()
            window.blit(self.victory,(550,266))
            self.is_victory=True
            window.blit(self.character.bMenu,(540,600))
            window.blit(self.character.restart,(500,500))
        self.Boss.draw(window,self.gold1_collect,self.gold2_collect,self.gold3_collect)
            
    def game_loop(self,key,mouse):
        self.key=key
        self.character.game_loop(key,mouse,self.is_victory,self.Boss.is_attack1,self.Boss.is_attack2,False,False,False,False)
        self.Boss.game_loop(self.character.c_x,self.character.c_is_attack1,self.character.c_is_attack2,self.character.c_status)
        if (self.character.get_Rect()).colliderect(self.Boss.b_x+168,607,30,30) and self.Boss.is_death==True and self.gold1_collect==False:
            self.character.c_gold+=10
            self.gold1_collect=True
        
        if (self.character.get_Rect()).colliderect(self.Boss.b_x+268,607,30,30) and self.Boss.is_death==True and self.gold2_collect==False:
            self.character.c_gold+=10
            self.gold2_collect=True
        
        if (self.character.get_Rect()).colliderect(self.Boss.b_x+368,607,30,30) and self.Boss.is_death==True and self.gold3_collect==False:
            self.character.c_gold+=10
            self.gold3_collect=True
        
        elif self.key[pygame.K_SPACE] and (self.character.c_status=="death" or self.is_victory):
            return "Test Level1"
        
        elif self.key[pygame.K_TAB] and (self.character.c_status=="death" or self.is_victory):
            return "Test Level0"