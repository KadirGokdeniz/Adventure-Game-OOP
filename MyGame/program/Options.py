import pygame
from Character import Character

class Options:
    def __init__(self,windows_width,windows_height):
        self.background=pygame.image.load("others\\TestLevels0\\background0.png").convert_alpha()
        self.background=pygame.transform.scale(self.background,(windows_width,windows_height))

        self.controller=pygame.image.load("others\\images\\controller.png").convert_alpha()
        self.controller=pygame.transform.scale(self.controller,(450,72))

        self.a=pygame.image.load("others\\images\\a.png").convert_alpha()
        self.a=pygame.transform.scale(self.a,(180,72))

        self.d=pygame.image.load("others\\images\\d.png").convert_alpha()
        self.d=pygame.transform.scale(self.d,(180,72))

        self.left=pygame.image.load("others\\images\\left.png").convert_alpha()
        self.left=pygame.transform.scale(self.left,(280,50))

        self.right=pygame.image.load("others\\images\\right.png").convert_alpha()
        self.right=pygame.transform.scale(self.right,(280,72))

        self.space=pygame.image.load("others\\images\\space.png").convert_alpha()
        self.space=pygame.transform.scale(self.space,(280,72))

        self.r1=pygame.image.load("others\\images\\r1.png").convert_alpha()
        self.r1=pygame.transform.scale(self.r1,(430,72))

        self.r2=pygame.image.load("others\\images\\r2.png").convert_alpha()
        self.r2=pygame.transform.scale(self.r2,(530,72))

        self.backspace=pygame.image.load("others\\images\\backspace.png").convert_alpha()
        self.backspace=pygame.transform.scale(self.backspace,(580,72))


        self.Charactera=Character(0)
        self.Characterd=Character(0)
        self.Characterr1=Character(0)
        self.Characterr2=Character(0)
        self.Characters=Character(0)
        self.Charactera1=Character(0)
        self.Charactera2=Character(0)

    def Draw(self,window):
        window.blit(self.background,(0,0))

        window.blit(self.controller,(500,20))
        window.blit(self.a,(200,150))
        window.blit(self.d,(200,300))
        window.blit(self.left,(1000,330))
        window.blit(self.right,(1000,470))
        window.blit(self.space,(1000,170))
        window.blit(self.r1,(200,450))
        window.blit(self.r2,(200,600))
        window.blit(self.backspace,(800,600))

        self.Charactera.Draw(window)
        self.Characterd.Draw(window)
        self.Characterr1.Draw(window)
        self.Characterr2.Draw(window)
        self.Characters.Draw(window)
        self.Charactera1.Draw(window)
        self.Charactera2.Draw(window)

    def GameLoop(self,key,mouse):
        self.key=key

        self.Charactera.c_y=100
        self.Characterd.c_y=250
        self.Characterr1.c_y=400
        self.Characterr2.c_y=550
        self.Characters.c_y=100
        self.Characters.c_x=800
        self.Charactera1.c_y=250
        self.Charactera1.c_x=800
        self.Charactera2.c_y=400
        self.Charactera2.c_x=800

        self.Charactera.c_direction=True
        self.Charactera.c_status="Run"
        self.Characterd.c_direction=False
        self.Characterd.c_status="Run"
        self.Characterr1.c_status="DrawSword"
        self.Characterr2.c_status="BackSword"
        self.Characters.c_status="Jump"
        self.Charactera1.c_status="AttackMode1"
        self.Charactera2.c_status="AttackMode2"

        self.Charactera.c_ranimation=self.Charactera.Animation(self.Charactera.c_rdelay,self.Charactera.c_ranimation,6)
        self.Characterd.c_ranimation=self.Characterd.Animation(self.Characterd.c_rdelay,self.Characterd.c_ranimation,6)
        self.Characterr1.c_danimation=self.Characterr1.Animation(self.Characterr1.c_ddelay,self.Characterr1.c_danimation,4,self.Characterr1.c_animation)
        self.Characterr2.c_danimation=self.Characterr2.Animation(self.Characterr2.c_ddelay,self.Characterr2.c_danimation,4,self.Characterr2.c_animation)
        self.Characters.c_janimation=self.Characters.Animation(self.Characters.c_jdelay,self.Characters.c_janimation,4,self.Characters.c_animation)
        self.Characters.c_fanimation=self.Characters.Animation(self.Characters.c_fdelay,self.Characters.c_fanimation,2,self.Characters.c_animation)
        self.Charactera1.c_a1animation=self.Charactera1.Animation(self.Charactera1.c_a1delay,self.Charactera1.c_a1animation,5,self.Charactera1.c_animation)
        self.Charactera2.c_a2animation=self.Charactera2.Animation(self.Charactera2.c_a2delay,self.Charactera2.c_a2animation,6,self.Charactera2.c_animation)

        if self.key[pygame.K_BACKSPACE]:
            return "Test Level0"