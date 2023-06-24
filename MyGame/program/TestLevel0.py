import pygame

class TestLevel0:
    def __init__(self,windows_width,windows_height):
        self.background=pygame.image.load("others\\TestLevels0\\background0.png").convert_alpha()
        self.background=pygame.transform.scale(self.background,(windows_width,windows_height))

        self.start=pygame.image.load("others\\images\\start.png").convert_alpha()
        self.start=pygame.transform.scale(self.start,(600,80))

        self.controllers=pygame.image.load("others\\images\\controllers.png").convert_alpha()
        self.controllers=pygame.transform.scale(self.controllers,(600,80))

    def Draw(self,window):
        window.blit(self.background,(0,0))
        window.blit(self.start,(500,300))
        window.blit(self.controllers,(500,500))

    def GameLoop(self,key,mouse):
        self.key=key
        self.mouse=mouse
        if self.key[pygame.K_SPACE]:
            return "Options"
        elif self.key[pygame.K_RETURN]:
            return "Test Level1"
        
