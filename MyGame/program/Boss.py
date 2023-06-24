from Material import *
import pygame

class Boss:
    def __init__(self,x):
        self.b_x=x
        self.b_y=300
        self.b_scale=(700,416.5)

        self.b_status="Breath"
        
        self.b_hp=10

        self.coin1=get_coin(self.b_x-100,600)
        self.coin2=get_coin(self.b_x,600)
        self.coin3=get_coin(self.b_x+100,600)

        self.b_banimation=0
        self.b_ranimation=0
        self.b_a1animation=0
        self.b_a2animation=0
        self.b_hanimation=0
        self.b_dthanimation=0

        self.b_time=pygame.time.get_ticks()
        self.b_time_hurt=pygame.time.get_ticks()

        self.b_rdelay=250
        self.b_bdelay=250
        self.b_a1delay=250
        self.b_a2delay=150
        self.b_hdelay=100
        self.b_dthdelay=300
        self.b_Path="others\\Boss\\"

        self.b_direction=False
        self.b_action_mode=False
        self.b_animation=False
        self.b_isDeath=False

        self.isAttack1=False
        self.isAttack2=False
        self.isAttack1End=False

        self.b_isAttack1=False
        self.b_isAttack2=False

        self.b_b1=pygame.image.load(self.b_Path+"b1.png").convert_alpha()
        self.b_b2=pygame.image.load(self.b_Path+"b2.png").convert_alpha()
        self.b_b3=pygame.image.load(self.b_Path+"b3.png").convert_alpha()
        self.b_b4=pygame.image.load(self.b_Path+"b4.png").convert_alpha()
        self.b_b5=pygame.image.load(self.b_Path+"b5.png").convert_alpha()
        self.b_b6=pygame.image.load(self.b_Path+"b6.png").convert_alpha()
        self.b_b7=pygame.image.load(self.b_Path+"b7.png").convert_alpha()
        self.b_b8=pygame.image.load(self.b_Path+"b8.png").convert_alpha()

        self.b_b1=pygame.transform.scale(self.b_b1,self.b_scale)
        self.b_b2=pygame.transform.scale(self.b_b2,self.b_scale)
        self.b_b3=pygame.transform.scale(self.b_b3,self.b_scale)
        self.b_b4=pygame.transform.scale(self.b_b4,self.b_scale)
        self.b_b5=pygame.transform.scale(self.b_b5,self.b_scale)
        self.b_b6=pygame.transform.scale(self.b_b6,self.b_scale)
        self.b_b7=pygame.transform.scale(self.b_b7,self.b_scale)
        self.b_b8=pygame.transform.scale(self.b_b8,self.b_scale)

        self.b_r1=pygame.image.load(self.b_Path+"r1.png").convert_alpha()
        self.b_r2=pygame.image.load(self.b_Path+"r2.png").convert_alpha()
        self.b_r3=pygame.image.load(self.b_Path+"r3.png").convert_alpha()
        self.b_r4=pygame.image.load(self.b_Path+"r4.png").convert_alpha()
        self.b_r5=pygame.image.load(self.b_Path+"r5.png").convert_alpha()
        self.b_r6=pygame.image.load(self.b_Path+"r6.png").convert_alpha()
        self.b_r7=pygame.image.load(self.b_Path+"r7.png").convert_alpha()
        self.b_r8=pygame.image.load(self.b_Path+"r8.png").convert_alpha()

        self.b_r1=pygame.transform.scale(self.b_r1,self.b_scale)
        self.b_r2=pygame.transform.scale(self.b_r2,self.b_scale)
        self.b_r3=pygame.transform.scale(self.b_r3,self.b_scale)
        self.b_r4=pygame.transform.scale(self.b_r4,self.b_scale)
        self.b_r5=pygame.transform.scale(self.b_r5,self.b_scale)
        self.b_r6=pygame.transform.scale(self.b_r6,self.b_scale)
        self.b_r7=pygame.transform.scale(self.b_r7,self.b_scale)
        self.b_r8=pygame.transform.scale(self.b_r8,self.b_scale)

        self.b_a11=pygame.image.load(self.b_Path+"a11.png").convert_alpha()
        self.b_a12=pygame.image.load(self.b_Path+"a12.png").convert_alpha()
        self.b_a13=pygame.image.load(self.b_Path+"a13.png").convert_alpha()
        self.b_a14=pygame.image.load(self.b_Path+"a14.png").convert_alpha()
        self.b_a15=pygame.image.load(self.b_Path+"a15.png").convert_alpha()
        self.b_a16=pygame.image.load(self.b_Path+"a16.png").convert_alpha()
        self.b_a17=pygame.image.load(self.b_Path+"a17.png").convert_alpha()
        self.b_a18=pygame.image.load(self.b_Path+"a18.png").convert_alpha()
        self.b_a19=pygame.image.load(self.b_Path+"a19.png").convert_alpha()
        self.b_a110=pygame.image.load(self.b_Path+"a110.png").convert_alpha()
        self.b_a111=pygame.image.load(self.b_Path+"a111.png").convert_alpha()

        self.b_a11=pygame.transform.scale(self.b_a11,self.b_scale)
        self.b_a12=pygame.transform.scale(self.b_a12,self.b_scale)
        self.b_a13=pygame.transform.scale(self.b_a13,self.b_scale)
        self.b_a14=pygame.transform.scale(self.b_a14,self.b_scale)
        self.b_a15=pygame.transform.scale(self.b_a15,self.b_scale)
        self.b_a16=pygame.transform.scale(self.b_a16,self.b_scale)
        self.b_a17=pygame.transform.scale(self.b_a17,self.b_scale)
        self.b_a18=pygame.transform.scale(self.b_a18,self.b_scale)
        self.b_a19=pygame.transform.scale(self.b_a19,self.b_scale)
        self.b_a110=pygame.transform.scale(self.b_a110,self.b_scale)
        self.b_a111=pygame.transform.scale(self.b_a111,self.b_scale)

        self.b_a21=pygame.image.load(self.b_Path+"a21.png").convert_alpha()
        self.b_a22=pygame.image.load(self.b_Path+"a22.png").convert_alpha()
        self.b_a23=pygame.image.load(self.b_Path+"a23.png").convert_alpha()
        self.b_a24=pygame.image.load(self.b_Path+"a24.png").convert_alpha()
        self.b_a25=pygame.image.load(self.b_Path+"a25.png").convert_alpha()
        self.b_a26=pygame.image.load(self.b_Path+"a26.png").convert_alpha()
        self.b_a27=pygame.image.load(self.b_Path+"a27.png").convert_alpha()
        self.b_a28=pygame.image.load(self.b_Path+"a28.png").convert_alpha()
        self.b_a29=pygame.image.load(self.b_Path+"a29.png").convert_alpha()
        self.b_a210=pygame.image.load(self.b_Path+"a210.png").convert_alpha()
        self.b_a211=pygame.image.load(self.b_Path+"a211.png").convert_alpha()
        self.b_a212=pygame.image.load(self.b_Path+"a212.png").convert_alpha()
        self.b_a213=pygame.image.load(self.b_Path+"a213.png").convert_alpha()
        self.b_a214=pygame.image.load(self.b_Path+"a214.png").convert_alpha()
        self.b_a215=pygame.image.load(self.b_Path+"a215.png").convert_alpha()
        self.b_a216=pygame.image.load(self.b_Path+"a216.png").convert_alpha()
        self.b_a217=pygame.image.load(self.b_Path+"a217.png").convert_alpha()
        self.b_a218=pygame.image.load(self.b_Path+"a218.png").convert_alpha()

        self.b_a21=pygame.transform.scale(self.b_a21,self.b_scale)
        self.b_a22=pygame.transform.scale(self.b_a22,self.b_scale)
        self.b_a23=pygame.transform.scale(self.b_a23,self.b_scale)
        self.b_a24=pygame.transform.scale(self.b_a24,self.b_scale)
        self.b_a25=pygame.transform.scale(self.b_a25,self.b_scale)
        self.b_a26=pygame.transform.scale(self.b_a26,self.b_scale)
        self.b_a27=pygame.transform.scale(self.b_a27,self.b_scale)
        self.b_a28=pygame.transform.scale(self.b_a28,self.b_scale)
        self.b_a29=pygame.transform.scale(self.b_a29,self.b_scale)
        self.b_a210=pygame.transform.scale(self.b_a210,self.b_scale)
        self.b_a211=pygame.transform.scale(self.b_a211,self.b_scale)
        self.b_a212=pygame.transform.scale(self.b_a212,self.b_scale)
        self.b_a213=pygame.transform.scale(self.b_a213,self.b_scale)
        self.b_a214=pygame.transform.scale(self.b_a214,self.b_scale)
        self.b_a215=pygame.transform.scale(self.b_a215,self.b_scale)
        self.b_a216=pygame.transform.scale(self.b_a216,self.b_scale)
        self.b_a217=pygame.transform.scale(self.b_a217,self.b_scale)
        self.b_a218=pygame.transform.scale(self.b_a218,self.b_scale)

        self.b_dth1=pygame.image.load(self.b_Path+"d1.png").convert_alpha()
        self.b_dth2=pygame.image.load(self.b_Path+"d2.png").convert_alpha()
        self.b_dth3=pygame.image.load(self.b_Path+"d3.png").convert_alpha()
        self.b_dth4=pygame.image.load(self.b_Path+"d4.png").convert_alpha()
        self.b_dth5=pygame.image.load(self.b_Path+"d5.png").convert_alpha()
        self.b_dth6=pygame.image.load(self.b_Path+"d6.png").convert_alpha()
        self.b_dth7=pygame.image.load(self.b_Path+"d7.png").convert_alpha()
        self.b_dth8=pygame.image.load(self.b_Path+"d8.png").convert_alpha()
        self.b_dth9=pygame.image.load(self.b_Path+"d9.png").convert_alpha()
        self.b_dth10=pygame.image.load(self.b_Path+"d10.png").convert_alpha()
        self.b_dth11=pygame.image.load(self.b_Path+"d11.png").convert_alpha()
        self.b_dth12=pygame.image.load(self.b_Path+"d12.png").convert_alpha()
        self.b_dth13=pygame.image.load(self.b_Path+"d13.png").convert_alpha()


        self.b_dth1=pygame.transform.scale(self.b_dth1,self.b_scale)
        self.b_dth2=pygame.transform.scale(self.b_dth2,self.b_scale)
        self.b_dth3=pygame.transform.scale(self.b_dth3,self.b_scale)
        self.b_dth4=pygame.transform.scale(self.b_dth4,self.b_scale)
        self.b_dth5=pygame.transform.scale(self.b_dth5,self.b_scale)
        self.b_dth6=pygame.transform.scale(self.b_dth6,self.b_scale)
        self.b_dth7=pygame.transform.scale(self.b_dth7,self.b_scale)
        self.b_dth8=pygame.transform.scale(self.b_dth8,self.b_scale)
        self.b_dth9=pygame.transform.scale(self.b_dth9,self.b_scale)
        self.b_dth10=pygame.transform.scale(self.b_dth10,self.b_scale)
        self.b_dth11=pygame.transform.scale(self.b_dth11,self.b_scale)
        self.b_dth12=pygame.transform.scale(self.b_dth12,self.b_scale)
        self.b_dth13=pygame.transform.scale(self.b_dth13,self.b_scale)

        self.b_h1=pygame.image.load(self.b_Path+"h1.png").convert_alpha()
        self.b_h2=pygame.image.load(self.b_Path+"h2.png").convert_alpha()
        self.b_h3=pygame.image.load(self.b_Path+"h3.png").convert_alpha()
        self.b_h4=pygame.image.load(self.b_Path+"h4.png").convert_alpha()
        self.b_h5=pygame.image.load(self.b_Path+"h5.png").convert_alpha()
        self.b_h6=pygame.image.load(self.b_Path+"h6.png").convert_alpha()

        self.b_h1=pygame.transform.scale(self.b_h1,self.b_scale)
        self.b_h2=pygame.transform.scale(self.b_h2,self.b_scale)
        self.b_h3=pygame.transform.scale(self.b_h3,self.b_scale)
        self.b_h4=pygame.transform.scale(self.b_h4,self.b_scale)
        self.b_h5=pygame.transform.scale(self.b_h5,self.b_scale)
        self.b_h6=pygame.transform.scale(self.b_h6,self.b_scale)

        self.b_breath_list=[self.b_b1,self.b_b2,self.b_b3,self.b_b4,self.b_b5,self.b_b6,self.b_b7,self.b_b8]
        self.b_run_list=[self.b_r1,self.b_r2,self.b_r3,self.b_r4,self.b_r5,self.b_r6,self.b_r7,self.b_r8]
        self.b_attack_mode1_list=[self.b_a11,self.b_a12,self.b_a13,self.b_a14,self.b_a15,self.b_a16,self.b_a17,self.b_a18,self.b_a19,self.b_a110,self.b_a111]
        self.b_attack_mode2_list=[self.b_a21,self.b_a22,self.b_a23,self.b_a24,self.b_a25,self.b_a26,self.b_a27,self.b_a28,self.b_a29,self.b_a210,self.b_a211,self.b_a212,self.b_a213,self.b_a214,self.b_a215,self.b_a216,self.b_a217,self.b_a218]
        self.b_death_list=[self.b_dth1,self.b_dth2,self.b_dth3,self.b_dth4,self.b_dth5,self.b_dth6,self.b_dth7,self.b_dth8,self.b_dth9,self.b_dth10,self.b_dth11,self.b_dth12,self.b_dth13]
        self.b_hurt_list=[self.b_h1,self.b_h2,self.b_h3,self.b_h4,self.b_h5,self.b_h6]

    def Draw(self,window,gold1collect,gold2collect,gold3collect):
        if self.b_status=="Breath":
            window.blit(pygame.transform.flip(self.b_breath_list[self.b_banimation],self.b_direction,False),(self.b_x,self.b_y))
        elif self.b_status=="Run":
            window.blit(pygame.transform.flip(self.b_run_list[self.b_ranimation],self.b_direction,False),(self.b_x,self.b_y))
        elif self.b_status=="AttackMode1":
            window.blit(pygame.transform.flip(self.b_attack_mode1_list[self.b_a1animation],self.b_direction,False),(self.b_x,self.b_y))
        elif self.b_status=="AttackMode2":
            window.blit(pygame.transform.flip(self.b_attack_mode2_list[self.b_a2animation],self.b_direction,False),(self.b_x,self.b_y))
        elif self.b_status=="Hurt":
            window.blit(pygame.transform.flip(self.b_hurt_list[self.b_hanimation],self.b_direction,False),(self.b_x,self.b_y))
        elif self.b_status=="Death":
            if self.b_dthanimation>=12:
                window.blit(pygame.transform.flip(self.b_death_list[12],self.b_direction,False),(self.b_x,self.b_y))
                if not gold1collect:
                    window.blit(self.coin1[0],(self.coin1[1],self.coin1[2]))
                if not gold2collect:
                    window.blit(self.coin2[0],(self.coin2[1],self.coin2[2]))
                if not gold3collect:
                    window.blit(self.coin3[0],(self.coin3[1],self.coin3[2]))
            else:
                window.blit(pygame.transform.flip(self.b_death_list[self.b_dthanimation],self.b_direction,False),(self.b_x,self.b_y))

    def Animation(self, Delay, animation_Number, limit_of_the_animation,condition=False,action_mode_end=False,status_mode_end="Breath"):
        if pygame.time.get_ticks()-self.b_time>Delay:
            animation_Number+=1
            if self.b_status=="Hurt" and animation_Number==1:
                if self.isAttack1:
                    self.b_hp-=1
                if self.isAttack2:
                    self.b_hp-=2
            if not(self.isAttack1 or self.isAttack2):
                self.isAttack1=False
                self.isAttack2=False
            if self.b_status=="AttackMode1" and animation_Number==4:
                self.b_isAttack1=True
            if self.b_status=="AttackMode2" and animation_Number==12:
                self.b_isAttack2=True
            if self.b_status=="AttackMode2" and animation_Number==17:
                self.isAttack1End=False
            if self.b_status=="AttackMode1" and animation_Number==10:
                self.isAttack1End=True
            if not((self.b_status=="AttackMode1" and animation_Number==4)or(self.b_status=="AttackMode2" and animation_Number==12)):
                self.b_isAttack2=False
                self.b_isAttack1=False
            if animation_Number== limit_of_the_animation and self.b_status!="Death":
                animation_Number=0
                if condition:
                    self.b_action_mode=action_mode_end
                    self.b_status=status_mode_end
                    self.b_animation=True
            else:
                status_mode_end="Death"
            self.b_time=pygame.time.get_ticks()
        return animation_Number
    
    def GameLoop(self,x,isAttack1,isAttack2,isDeath):
        #Action
        if isAttack1:
            self.isAttack1=True
        if isAttack2:
            self.isAttack2=True

        if ((x-180>=self.b_x)and not self.b_isDeath):
            self.b_direction=False
        if ((x-180<self.b_x)and not self.b_isDeath):
            self.b_direction=True
        if ((-100<=self.b_x-x<=600)and not self.b_isDeath):
            self.b_status="Run"
            self.b_animation=True
            self.b_action_mode=True
            self.b_x-=0.75
        if ((300<=x-self.b_x<=850)and not self.b_isDeath):
            self.b_status="Run"
            self.b_animation=True
            self.b_action_mode=True
            self.b_x+=0.75
        if self.b_direction==False and x-self.b_x<=300:
            if ((isAttack1 or isAttack2)and not self.b_isDeath):
                self.b_status="Hurt"
                if self.b_hp<=0:
                    self.b_status="Death"
                    self.b_isDeath=True
            elif (not(isAttack1 or isAttack2)and not self.b_isDeath):
                if self.isAttack1End:
                    self.b_status="AttackMode2"
                if not self.isAttack1End:
                    self.b_status="AttackMode1"
            self.b_animation=True
        if self.b_direction==True and x-self.b_x>=100:
            if ((isAttack1 or isAttack2)and not self.b_isDeath):
                self.b_status="Hurt"
                if self.b_hp<=0:
                    self.b_status="Death"
                    self.b_isDeath=True
            elif (not(isAttack1 or isAttack2)and not self.b_isDeath):
                if self.isAttack1End:
                    self.b_status="AttackMode2"
                if not self.isAttack1End:
                    self.b_status="AttackMode1"
            self.b_animation=True
        #States
        if self.b_action_mode==True:
            if self.b_status=="Run":
                self.b_ranimation=self.Animation(self.b_rdelay,self.b_ranimation,8)
            if self.b_status=="AttackMode1":
                self.b_a1animation=self.Animation(self.b_a1delay,self.b_a1animation,11,self.b_animation,True,"AttackMode2")
                if 0<=self.b_a1animation<11 and isDeath=="Death":
                    self.b_a1animation=0
                    self.b_status="Breath"

            if self.b_status=="AttackMode2":
                self.b_a2animation=self.Animation(self.b_a2delay,self.b_a2animation,18)
                if 0<=self.b_a2animation<=18 and isDeath=="Death":
                    self.b_a2animation=0
                    self.b_status="Breath"
                
            
            elif self.b_status=="Breath":
                self.b_banimation=self.Animation(self.b_bdelay,self.b_banimation,8)

            elif self.b_status=="Hurt":
                self.b_hanimation=self.Animation(self.b_hdelay,self.b_hanimation,6)
                self.b_a1animation=0
                self.b_a2animation=0

            elif self.b_status=="Death":
                self.b_dthanimation=self.Animation(self.b_dthdelay,self.b_dthanimation,13)

        else:
            if self.b_status=="Breath":
                self.b_banimation=self.Animation(self.b_bdelay,self.b_banimation,8)