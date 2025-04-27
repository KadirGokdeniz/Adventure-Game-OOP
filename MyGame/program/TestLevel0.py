import pygame

class TestLevel0:
    def __init__(self,windows_width,windows_height):
        self.background = self.resource_manager.load_image("others\\TestLevels0\\background0.png",(windows_width,windows_height))

        self.start = self.resource_manager.load_image("others\\images\\start.png",(600,80))

        self.controllers = self.resource_manager.load_image("others\\images\\controllers.png",(600,80))

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
        
