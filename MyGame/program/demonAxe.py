import pygame
from Material import *

class demonAxe:
    def __init__(self,x):
        self.d_x=x
        self.d_y=440
        self.d_scale=(375,277.5)

        self.d_status="Breath"
        self.coin=get_coin(self.d_x-100,600)
        self.d_hp=3

        self.d_banimation=0
        self.d_ranimation=0
        self.d_a1animation=0
        self.d_a2animation=0
        self.d_hanimation=0
        self.d_dthanimation=0
        
        self.attack_list=["AttackMode1","Breath","AttackMode2","Breath"]

        self.d_time=pygame.time.get_ticks()
        self.d_time_hurt=pygame.time.get_ticks()

        self.d_rdelay=250
        self.d_bdelay=250
        self.d_a1delay=300
        self.d_a2delay=300
        self.d_hdelay=100
        self.d_dthdelay=300
        self.d_Path="others\\DemonAxe\\"

        self.d_direction=False
        self.d_action_mode=False
        self.d_animation=False
        self.d_isDeath=False
        self.d_isAttack1=False
        self.d_isAttack2=False
        
        self.isAttack1=False
        self.isAttack2=False

        self.d_b1=pygame.image.load(self.d_Path+"b1.png").convert_alpha()
        self.d_b2=pygame.image.load(self.d_Path+"b2.png").convert_alpha()
        self.d_b3=pygame.image.load(self.d_Path+"b3.png").convert_alpha()
        self.d_b4=pygame.image.load(self.d_Path+"b4.png").convert_alpha()
        self.d_b5=pygame.image.load(self.d_Path+"b5.png").convert_alpha()
        self.d_b6=pygame.image.load(self.d_Path+"b6.png").convert_alpha()

        self.d_b1=pygame.transform.scale(self.d_b1,self.d_scale)
        self.d_b2=pygame.transform.scale(self.d_b2,self.d_scale)
        self.d_b3=pygame.transform.scale(self.d_b3,self.d_scale)
        self.d_b4=pygame.transform.scale(self.d_b4,self.d_scale)
        self.d_b5=pygame.transform.scale(self.d_b5,self.d_scale)
        self.d_b6=pygame.transform.scale(self.d_b6,self.d_scale)

        self.d_r1=pygame.image.load(self.d_Path+"r1.png").convert_alpha()
        self.d_r2=pygame.image.load(self.d_Path+"r2.png").convert_alpha()
        self.d_r3=pygame.image.load(self.d_Path+"r3.png").convert_alpha()
        self.d_r4=pygame.image.load(self.d_Path+"r4.png").convert_alpha()
        self.d_r5=pygame.image.load(self.d_Path+"r5.png").convert_alpha()
        self.d_r6=pygame.image.load(self.d_Path+"r6.png").convert_alpha()

        self.d_r1=pygame.transform.scale(self.d_r1,self.d_scale)
        self.d_r2=pygame.transform.scale(self.d_r2,self.d_scale)
        self.d_r3=pygame.transform.scale(self.d_r3,self.d_scale)
        self.d_r4=pygame.transform.scale(self.d_r4,self.d_scale)
        self.d_r5=pygame.transform.scale(self.d_r5,self.d_scale)
        self.d_r6=pygame.transform.scale(self.d_r6,self.d_scale)

        self.d_a11=pygame.image.load(self.d_Path+"a11.png").convert_alpha()
        self.d_a12=pygame.image.load(self.d_Path+"a12.png").convert_alpha()
        self.d_a13=pygame.image.load(self.d_Path+"a13.png").convert_alpha()
        self.d_a14=pygame.image.load(self.d_Path+"a14.png").convert_alpha()
        self.d_a15=pygame.image.load(self.d_Path+"a15.png").convert_alpha()
        self.d_a16=pygame.image.load(self.d_Path+"a16.png").convert_alpha()

        self.d_a11=pygame.transform.scale(self.d_a11,self.d_scale)
        self.d_a12=pygame.transform.scale(self.d_a12,self.d_scale)
        self.d_a13=pygame.transform.scale(self.d_a13,self.d_scale)
        self.d_a14=pygame.transform.scale(self.d_a14,self.d_scale)
        self.d_a15=pygame.transform.scale(self.d_a15,self.d_scale)
        self.d_a16=pygame.transform.scale(self.d_a16,self.d_scale)

        self.d_a21=pygame.image.load(self.d_Path+"a21.png").convert_alpha()
        self.d_a22=pygame.image.load(self.d_Path+"a22.png").convert_alpha()
        self.d_a23=pygame.image.load(self.d_Path+"a23.png").convert_alpha()
        self.d_a24=pygame.image.load(self.d_Path+"a24.png").convert_alpha()
        self.d_a25=pygame.image.load(self.d_Path+"a25.png").convert_alpha()
        self.d_a26=pygame.image.load(self.d_Path+"a26.png").convert_alpha()

        self.d_a21=pygame.transform.scale(self.d_a21,self.d_scale)
        self.d_a22=pygame.transform.scale(self.d_a22,self.d_scale)
        self.d_a23=pygame.transform.scale(self.d_a23,self.d_scale)
        self.d_a24=pygame.transform.scale(self.d_a24,self.d_scale)
        self.d_a25=pygame.transform.scale(self.d_a25,self.d_scale)
        self.d_a26=pygame.transform.scale(self.d_a26,self.d_scale)

        self.d_dth1=pygame.image.load(self.d_Path+"d1.png").convert_alpha()
        self.d_dth2=pygame.image.load(self.d_Path+"d2.png").convert_alpha()
        self.d_dth3=pygame.image.load(self.d_Path+"d3.png").convert_alpha()
        self.d_dth4=pygame.image.load(self.d_Path+"d4.png").convert_alpha()

        self.d_dth1=pygame.transform.scale(self.d_dth1,self.d_scale)
        self.d_dth2=pygame.transform.scale(self.d_dth2,self.d_scale)
        self.d_dth3=pygame.transform.scale(self.d_dth3,self.d_scale)
        self.d_dth4=pygame.transform.scale(self.d_dth4,self.d_scale)

        self.d_h1=pygame.image.load(self.d_Path+"h1.png").convert_alpha()
        self.d_h2=pygame.image.load(self.d_Path+"h2.png").convert_alpha()
        self.d_h3=pygame.image.load(self.d_Path+"h3.png").convert_alpha()

        self.d_h1=pygame.transform.scale(self.d_h1,self.d_scale)
        self.d_h2=pygame.transform.scale(self.d_h2,self.d_scale)
        self.d_h3=pygame.transform.scale(self.d_h3,self.d_scale)

        self.d_breath_list=[self.d_b1,self.d_b2,self.d_b3,self.d_b4,self.d_b5,self.d_b6]
        self.d_run_list=[self.d_r1,self.d_r2,self.d_r3,self.d_r4,self.d_r5,self.d_r6]
        self.d_attack_mode1_list=[self.d_a11,self.d_a12,self.d_a13,self.d_a14,self.d_a15,self.d_a16]
        self.d_attack_mode2_list=[self.d_a21,self.d_a22,self.d_a23,self.d_a24,self.d_a25,self.d_a26]
        self.d_death_list=[self.d_dth1,self.d_dth2,self.d_dth3,self.d_dth4]
        self.d_hurt_list=[self.d_h1,self.d_h2,self.d_h3]

    def Draw(self,window):
        if self.d_status=="Breath":
            window.blit(pygame.transform.flip(self.d_breath_list[self.d_banimation],self.d_direction,False),(self.d_x,self.d_y))
        elif self.d_status=="Run":
            window.blit(pygame.transform.flip(self.d_run_list[self.d_ranimation],self.d_direction,False),(self.d_x,self.d_y))
        elif self.d_status=="AttackMode1":
            window.blit(pygame.transform.flip(self.d_attack_mode1_list[self.d_a1animation],self.d_direction,False),(self.d_x,self.d_y))
        elif self.d_status=="AttackMode2":
            window.blit(pygame.transform.flip(self.d_attack_mode2_list[self.d_a2animation],self.d_direction,False),(self.d_x,self.d_y))
        elif self.d_status=="Hurt":
            window.blit(pygame.transform.flip(self.d_hurt_list[self.d_hanimation],self.d_direction,False),(self.d_x,self.d_y))
            self.d_a1animation=0
            self.d_a2animation=0
        elif self.d_status=="Death":
            if self.d_dthanimation>=3:
                window.blit(pygame.transform.flip(self.d_death_list[3],self.d_direction,False),(self.d_x,self.d_y))
                window.blit(self.coin[0],(self.coin[1],self.coin[2]))
            else:
                window.blit(pygame.transform.flip(self.d_death_list[self.d_dthanimation],self.d_direction,False),(self.d_x,self.d_y))

    def Animation(self, Delay, animation_Number, limit_of_the_animation,condition=False,action_mode_end=False,status_mode_end="Breath"):
        if pygame.time.get_ticks()-self.d_time>Delay:
            animation_Number+=1
            if self.d_status=="Hurt" and animation_Number==1:
                if self.isAttack1:
                    self.d_hp-=1
                if self.isAttack2:
                    self.d_hp-=2
            if self.d_status=="AttackMode1" and animation_Number==3:
                self.d_isAttack1=True
            if self.d_status=="AttackMode2" and animation_Number==3:
                self.d_isAttack2=True
            if not(self.isAttack1 or self.isAttack2):
                self.isAttack1=False
                self.isAttack2=False
            if not((self.d_status=="AttackMode1" and animation_Number==3)or(self.d_status=="AttackMode2" and animation_Number==3)):
                self.d_isAttack2=False
                self.d_isAttack1=False
            if animation_Number== limit_of_the_animation and self.d_status!="Death":
                animation_Number=0
                if condition:
                    self.d_action_mode=action_mode_end
                    self.d_status=status_mode_end
                    self.d_animation=False
            else:
                status_mode_end="Death"
            self.d_time=pygame.time.get_ticks()
        return animation_Number
    
    def GameLoop(self,x,isAttack1,isAttack2,isDeath):
        #Action
        if isAttack1:
            self.isAttack1=True
        if isAttack2:
            self.isAttack2=True

        if ((x-31>self.d_x)and not self.d_isDeath):
            self.d_direction=False
            self.coin[1]=self.d_x+150
        if ((x-31<self.d_x)and not self.d_isDeath):
            self.d_direction=True
            self.coin[1]=self.d_x+150
        if ((0<self.d_x-x<=500)and not self.d_isDeath):
            self.d_status="Run"
            self.d_animation=True
            self.d_action_mode=True
            self.d_x-=0.75
        if ((150<=x-self.d_x<=662)and not self.d_isDeath):
            self.d_status="Run"
            self.d_animation=True
            self.d_action_mode=True
            self.d_x+=0.75
        if self.d_direction==False and x-self.d_x<=150:
            if ((isAttack1 or isAttack2)and not self.d_isDeath):
                self.d_status="Hurt"
                if self.d_hp<=0:
                    self.d_status="Death"
                    self.d_isDeath=True
            if (not(isAttack1 or isAttack2)and not self.d_isDeath):
                self.d_status="AttackMode1"
            self.d_animation=True
        if self.d_direction==True and x-self.d_x>=0:
            if ((isAttack1 or isAttack2)and not self.d_isDeath):
                self.d_status="Hurt"
                if self.d_hp<=0:
                    self.d_status="Death"
                    self.d_isDeath=True
            if (not(isAttack1 or isAttack2)and not self.d_isDeath):
                self.d_status="AttackMode1"
            self.d_animation=True
        #States
        if self.d_action_mode==True:
            if self.d_status=="Run":
                self.d_ranimation=self.Animation(self.d_rdelay,self.d_ranimation,6)

            elif self.d_status=="AttackMode1":
                self.d_a1animation=self.Animation(self.d_a1delay,self.d_a1animation,6)
                if 0<=self.d_a1animation<=6 and isDeath=="Death":
                    self.d_a1animation=0
                    self.d_status="Breath"

            elif self.d_status=="AttackMode2":
                self.d_a2animation=self.Animation(self.d_a2delay,self.d_a2animation,6)
                if 0<=self.d_a1animation<=6 and isDeath=="Death":
                    self.d_a1animation=0
                    self.d_status="Breath"
            
            elif self.d_status=="Breath":
                self.d_banimation=self.Animation(self.d_bdelay,self.d_banimation,6)

            elif self.d_status=="Hurt":
                self.d_hanimation=self.Animation(self.d_hdelay,self.d_hanimation,3)

            elif self.d_status=="Death":
                self.d_dthanimation=self.Animation(self.d_dthdelay,self.d_dthanimation,3)

        else:
            if self.d_status=="Breath":
                self.d_banimation=self.Animation(self.d_bdelay,self.d_banimation,6)
