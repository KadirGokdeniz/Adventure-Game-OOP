import pygame
import json

class Character:
    def __init__(self,level):
        self.c_x=0
        self.c_y=550
        self.level=level
        self.c_gold=0
        self.c_hp=10
        if level==1:
           self.c_y=550
           self.Character_Save_Files()
        elif level ==2:
            self.c_y=570
            self.Character_Load_Files()
        self.c_scale=(200,148)
        
        self.c_status="Breath"
        self.c_speed=1.25
        if level!=0:
            self.c_gold=self.c_dictionary["Gold"]
            self.c_hp=self.c_dictionary["Hp"]

        self.isAttack11=False
        self.isAttack12=False
        self.isAttack13=False
        self.isAttack21=False
        self.isAttack22=False
        self.isAttack23=False


        self.c_banimation=0
        self.c_sanimation=0
        self.c_ranimation=0
        self.c_danimation=0
        self.c_a1animation=0
        self.c_a2animation=0
        self.c_janimation=0
        self.c_fanimation=0
        self.c_hanimation=0
        self.c_dthanimation=0

        self.c_time=pygame.time.get_ticks()
        self.c_time_hurt=pygame.time.get_ticks()
        self.c_time_jump=pygame.time.get_ticks()
        self.c_time_fall=pygame.time.get_ticks()
        
        self.c_rdelay=250
        self.c_bdelay=250
        self.c_sdelay=250
        self.c_ddelay=200
        self.c_a1delay=150
        self.c_a2delay=300
        self.c_jdelay=200
        self.c_fdelay=200
        self.c_hdelay=150
        self.c_dthdelay=300
        self.c_Path="others\\Character_images\\"

        self.c_action_mode=False
        self.c_direction=False
        self.c_animation=False
        self.c_isAttack1=False
        self.c_isAttack2=False
        self.c_isJump=False

        self.isRestart=False
        self.backMenu=False

        self.bMenu=pygame.image.load("others\\images\\bMenu.png").convert_alpha()
        self.bMenu=pygame.transform.scale(self.bMenu,(400,62))

        self.defeat=pygame.image.load("others\\images\\defeat.png").convert_alpha()
        self.defeat=pygame.transform.scale(self.defeat,(400,200))

        self.restart=pygame.image.load("others\\images\\restart.png").convert_alpha()
        self.restart=pygame.transform.scale(self.restart,(500,75))

        self.c_b1=pygame.image.load(self.c_Path+"b1.png").convert_alpha()
        self.c_b2=pygame.image.load(self.c_Path+"b2.png").convert_alpha()
        self.c_b3=pygame.image.load(self.c_Path+"b3.png").convert_alpha()
        self.c_b4=pygame.image.load(self.c_Path+"b4.png").convert_alpha()

        self.c_b1=pygame.transform.scale(self.c_b1,self.c_scale)
        self.c_b2=pygame.transform.scale(self.c_b2,self.c_scale)
        self.c_b3=pygame.transform.scale(self.c_b3,self.c_scale)
        self.c_b4=pygame.transform.scale(self.c_b4,self.c_scale)

        self.c_s1=pygame.image.load(self.c_Path+"s1.png").convert_alpha()
        self.c_s2=pygame.image.load(self.c_Path+"s2.png").convert_alpha()
        self.c_s3=pygame.image.load(self.c_Path+"s3.png").convert_alpha()
        self.c_s4=pygame.image.load(self.c_Path+"s4.png").convert_alpha()

        self.c_s1=pygame.transform.scale(self.c_s1,self.c_scale)
        self.c_s2=pygame.transform.scale(self.c_s2,self.c_scale)
        self.c_s3=pygame.transform.scale(self.c_s3,self.c_scale)
        self.c_s4=pygame.transform.scale(self.c_s4,self.c_scale)

        self.c_r1=pygame.image.load(self.c_Path+"r1.png").convert_alpha()
        self.c_r2=pygame.image.load(self.c_Path+"r2.png").convert_alpha()
        self.c_r3=pygame.image.load(self.c_Path+"r3.png").convert_alpha()
        self.c_r4=pygame.image.load(self.c_Path+"r4.png").convert_alpha()
        self.c_r5=pygame.image.load(self.c_Path+"r5.png").convert_alpha()
        self.c_r6=pygame.image.load(self.c_Path+"r6.png").convert_alpha()

        self.c_r1=pygame.transform.scale(self.c_r1,self.c_scale)
        self.c_r2=pygame.transform.scale(self.c_r2,self.c_scale)
        self.c_r3=pygame.transform.scale(self.c_r3,self.c_scale)
        self.c_r4=pygame.transform.scale(self.c_r4,self.c_scale)
        self.c_r5=pygame.transform.scale(self.c_r5,self.c_scale)
        self.c_r6=pygame.transform.scale(self.c_r6,self.c_scale)

        self.c_d1=pygame.image.load(self.c_Path+"d1.png").convert_alpha()
        self.c_d2=pygame.image.load(self.c_Path+"d2.png").convert_alpha()
        self.c_d3=pygame.image.load(self.c_Path+"d3.png").convert_alpha()
        self.c_d4=pygame.image.load(self.c_Path+"d4.png").convert_alpha()

        self.c_d1=pygame.transform.scale(self.c_r1,self.c_scale)
        self.c_d2=pygame.transform.scale(self.c_d2,self.c_scale)
        self.c_d3=pygame.transform.scale(self.c_d3,self.c_scale)
        self.c_d4=pygame.transform.scale(self.c_d4,self.c_scale)

        self.c_attackmode_1_1=pygame.image.load(self.c_Path+"a11.png").convert_alpha()
        self.c_attackmode_1_2=pygame.image.load(self.c_Path+"a12.png").convert_alpha()
        self.c_attackmode_1_3=pygame.image.load(self.c_Path+"a13.png").convert_alpha()
        self.c_attackmode_1_4=pygame.image.load(self.c_Path+"a14.png").convert_alpha()
        self.c_attackmode_1_5=pygame.image.load(self.c_Path+"a15.png").convert_alpha()

        self.c_attackmode_1_1=pygame.transform.scale(self.c_attackmode_1_1,self.c_scale)
        self.c_attackmode_1_2=pygame.transform.scale(self.c_attackmode_1_2,self.c_scale)
        self.c_attackmode_1_3=pygame.transform.scale(self.c_attackmode_1_3,self.c_scale)
        self.c_attackmode_1_4=pygame.transform.scale(self.c_attackmode_1_4,self.c_scale)
        self.c_attackmode_1_5=pygame.transform.scale(self.c_attackmode_1_5,self.c_scale)

        self.c_attackmode_2_1=pygame.image.load(self.c_Path+"a21.png").convert_alpha()
        self.c_attackmode_2_2=pygame.image.load(self.c_Path+"a22.png").convert_alpha()
        self.c_attackmode_2_3=pygame.image.load(self.c_Path+"a23.png").convert_alpha()
        self.c_attackmode_2_4=pygame.image.load(self.c_Path+"a24.png").convert_alpha()
        self.c_attackmode_2_5=pygame.image.load(self.c_Path+"a25.png").convert_alpha()
        self.c_attackmode_2_6=pygame.image.load(self.c_Path+"a26.png").convert_alpha()

        self.c_attackmode_2_1=pygame.transform.scale(self.c_attackmode_2_1,self.c_scale)
        self.c_attackmode_2_2=pygame.transform.scale(self.c_attackmode_2_2,self.c_scale)
        self.c_attackmode_2_3=pygame.transform.scale(self.c_attackmode_2_3,self.c_scale)
        self.c_attackmode_2_4=pygame.transform.scale(self.c_attackmode_2_4,self.c_scale)
        self.c_attackmode_2_5=pygame.transform.scale(self.c_attackmode_2_5,self.c_scale)
        self.c_attackmode_2_6=pygame.transform.scale(self.c_attackmode_2_6,self.c_scale)

        self.c_j1=pygame.image.load(self.c_Path+"j1.png").convert_alpha()
        self.c_j2=pygame.image.load(self.c_Path+"j2.png").convert_alpha()
        self.c_j3=pygame.image.load(self.c_Path+"j3.png").convert_alpha()
        self.c_j4=pygame.image.load(self.c_Path+"j4.png").convert_alpha()

        self.c_f1=pygame.image.load(self.c_Path+"f1.png").convert_alpha()
        self.c_f2=pygame.image.load(self.c_Path+"f2.png").convert_alpha()

        self.c_j1=pygame.transform.scale(self.c_j1,self.c_scale)
        self.c_j2=pygame.transform.scale(self.c_j2,self.c_scale)
        self.c_j3=pygame.transform.scale(self.c_j3,self.c_scale)
        self.c_j4=pygame.transform.scale(self.c_j4,self.c_scale)

        self.c_f1=pygame.transform.scale(self.c_f1,self.c_scale)
        self.c_f2=pygame.transform.scale(self.c_f2,self.c_scale)
        
        self.c_h1=pygame.image.load(self.c_Path+"h1.png").convert_alpha()
        self.c_h2=pygame.image.load(self.c_Path+"h2.png").convert_alpha()
        self.c_h3=pygame.image.load(self.c_Path+"h3.png").convert_alpha()

        self.c_h1=pygame.transform.scale(self.c_h1,self.c_scale)
        self.c_h2=pygame.transform.scale(self.c_h2,self.c_scale)
        self.c_h3=pygame.transform.scale(self.c_h3,self.c_scale)

        self.c_dth1=pygame.image.load(self.c_Path+"dth1.png").convert_alpha()
        self.c_dth2=pygame.image.load(self.c_Path+"dth2.png").convert_alpha()
        self.c_dth3=pygame.image.load(self.c_Path+"dth3.png").convert_alpha()
        self.c_dth4=pygame.image.load(self.c_Path+"dth4.png").convert_alpha()
        self.c_dth5=pygame.image.load(self.c_Path+"dth5.png").convert_alpha()
        self.c_dth6=pygame.image.load(self.c_Path+"dth6.png").convert_alpha()

        self.c_dth1=pygame.transform.scale(self.c_dth1,self.c_scale)
        self.c_dth2=pygame.transform.scale(self.c_dth2,self.c_scale)
        self.c_dth3=pygame.transform.scale(self.c_dth3,self.c_scale)
        self.c_dth4=pygame.transform.scale(self.c_dth4,self.c_scale)
        self.c_dth5=pygame.transform.scale(self.c_dth5,self.c_scale)
        self.c_dth6=pygame.transform.scale(self.c_dth6,self.c_scale)

        self.c_breath=[self.c_b1,self.c_b2,self.c_b3,self.c_b4]
        self.c_sword=[self.c_s1,self.c_s2,self.c_s3,self.c_s4]
        self.c_run=[self.c_r1,self.c_r2,self.c_r3,self.c_r4,self.c_r5,self.c_r6]
        self.c_drawSword=[self.c_d1,self.c_d2,self.c_d3,self.c_d4]
        self.c_backSword=[self.c_d4,self.c_d3,self.c_d2,self.c_d1]
        self.c_attack_mode_1_list=[self.c_attackmode_1_1,self.c_attackmode_1_2,self.c_attackmode_1_3,self.c_attackmode_1_4,self.c_attackmode_1_5]
        self.c_attack_mode_2_list=[self.c_attackmode_2_1,self.c_attackmode_2_2,self.c_attackmode_2_3,self.c_attackmode_2_4,self.c_attackmode_2_5,self.c_attackmode_2_6]
        self.c_jump_list=[self.c_j1,self.c_j2,self.c_j3,self.c_j4]
        self.c_fall_list=[self.c_f1,self.c_f2]
        self.c_hurt_list=[self.c_h1,self.c_h2,self.c_h3]
        self.c_death_list=[self.c_dth1,self.c_dth2,self.c_dth3,self.c_dth4,self.c_dth5,self.c_dth6]

    def Draw(self,window):
        if self.c_status=="Breath":
            window.blit(pygame.transform.flip(self.c_breath[self.c_banimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="Sword":
            window.blit(pygame.transform.flip(self.c_sword[self.c_sanimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="Run":
            window.blit(pygame.transform.flip(self.c_run[self.c_ranimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="DrawSword":
            window.blit(pygame.transform.flip(self.c_drawSword[self.c_danimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="BackSword":
            window.blit(pygame.transform.flip(self.c_backSword[self.c_danimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="AttackMode1":
            window.blit(pygame.transform.flip(self.c_attack_mode_1_list[self.c_a1animation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="AttackMode2":
            window.blit(pygame.transform.flip(self.c_attack_mode_2_list[self.c_a2animation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="Fall":
            window.blit(pygame.transform.flip(self.c_fall_list[self.c_fanimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="Jump":
            window.blit(pygame.transform.flip(self.c_jump_list[self.c_janimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="Hurt":
            window.blit(pygame.transform.flip(self.c_hurt_list[self.c_hanimation],self.c_direction,False),(self.c_x,self.c_y))
        elif self.c_status=="Death":
            if self.c_dthanimation>=6:
                window.blit(pygame.transform.flip(self.c_death_list[5],self.c_direction,False),(self.c_x,self.c_y))
                window.blit(self.defeat,(550,266))
                window.blit(self.restart,(500,500))
                window.blit(self.bMenu,(540,600))
            else:
                window.blit(pygame.transform.flip(self.c_death_list[self.c_dthanimation],self.c_direction,False),(self.c_x,self.c_y))
    
    def Character_Save_Files(self):
        self.c_dictionary= {"Gold":self.c_gold, "Hp":self.c_hp}
        json.dump(self.c_dictionary,open("others\\CharacterData.txt","w"))

    def Character_Load_Files(self):
        self.c_dictionary=json.load(open("others\\CharacterData.txt","r"))

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