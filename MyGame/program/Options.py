import pygame
from Character import Character

class Options:
    def __init__(self,windows_width,windows_height):
        self.background = self.resource_manager.load_image("others\\TestLevels0\\background0.png", (windows_width,windows_height))

        self.controller = self.resource_manager.load_image("others\\images\\controller.png", (450,72))

        self.a = self.resource_manager.load_image("others\\images\\a.png", (450,72))

        self.d = self.resource_manager.load_image("others\\images\\d.png", (180,72))

        self.left = self.resource_manager.load_image("others\\images\\left.png", (280,50))

        self.right = self.resource_manager.load_image("others\\images\\right.png", (280,72))

        self.space = self.resource_manager.load_image("others\\images\\space.png", (280,72))

        self.r1 = self.resource_manager.load_image("others\\images\\r1.png", (430,72))

        self.r2 = self.resource_manager.load_image("others\\images\\r2.png", (530,72))

        self.backspace= self.resource_manager.load_image("others\\images\\backspace.png", (580,72))


        self.charactera=Character(0)
        self.characterd=Character(0)
        self.characterr1=Character(0)
        self.characterr2=Character(0)
        self.characters=Character(0)
        self.charactera1=Character(0)
        self.charactera2=Character(0)

    def draw(self,window):
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

        self.charactera.draw(window)
        self.characterd.draw(window)
        self.characterr1.draw(window)
        self.characterr2.draw(window)
        self.characters.draw(window)
        self.charactera1.draw(window)
        self.charactera2.draw(window)

    def game_loop(self,key,mouse):
        self.key=key

        self.charactera.c_y=100
        self.characterd.c_y=250
        self.characterr1.c_y=400
        self.characterr2.c_y=550
        self.characters.c_y=100
        self.characters.c_x=800
        self.charactera1.c_y=250
        self.charactera1.c_x=800
        self.charactera2.c_y=400
        self.charactera2.c_x=800

        self.charactera.c_direction=True
        self.charactera.c_status="run"
        self.characterd.c_direction=False
        self.characterd.c_status="run"
        self.characterr1.c_status="draw_sword"
        self.characterr2.c_status="back_sword"
        self.characters.c_status="jump"
        self.charactera1.c_status="attack_mode1"
        self.charactera2.c_status="attack_mode2"

        self.charactera.c_ranimation=self.charactera.Animation(self.charactera.c_rdelay,self.charactera.c_ranimation,6)
        self.characterd.c_ranimation=self.characterd.Animation(self.characterd.c_rdelay,self.characterd.c_ranimation,6)
        self.characterr1.c_danimation=self.characterr1.Animation(self.characterr1.c_ddelay,self.characterr1.c_danimation,4,self.characterr1.c_animation)
        self.characterr2.c_danimation=self.characterr2.Animation(self.characterr2.c_ddelay,self.characterr2.c_danimation,4,self.characterr2.c_animation)
        self.characters.c_janimation=self.characters.Animation(self.characters.c_jdelay,self.characters.c_janimation,4,self.characters.c_animation)
        self.characters.c_fanimation=self.characters.Animation(self.characters.c_fdelay,self.characters.c_fanimation,2,self.characters.c_animation)
        self.charactera1.c_a1animation=self.charactera1.Animation(self.charactera1.c_a1delay,self.charactera1.c_a1animation,5,self.charactera1.c_animation)
        self.charactera2.c_a2animation=self.charactera2.Animation(self.charactera2.c_a2delay,self.charactera2.c_a2animation,6,self.charactera2.c_animation)

        if self.key[pygame.K_BACKSPACE]:
            return "Test Level0"