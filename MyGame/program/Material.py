import pygame

def get_coin(x,y):
    coin=pygame.image.load("others\\images\\goldcoin.png").convert_alpha()
    coin=pygame.transform.scale(coin,(40,40))
    return [coin ,x ,y,pygame.Rect(x,y+15,25,25)]