import pygame
import math
import sys

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# class freccia:
#     def __init__(self, dimx=0 , dimy=0 , x=0 , y=0 ) -> None:
#         self.dimx = dimx
#         self.dimy = dimy
#         self.x = x
#         self.y = y
#         self.rect = pygame.Rect(x, y, dimx, dimx)
#         self.img = pygame.image.load("freccia.png")
#         self.img = pygame.transform.scale(self.img, (self.rect.width, self.rect.height))
#         screen.blit(self.img, (x, y))

class freccia:
    def __init__(self, screen,  dim = [30,30], pos = [0,0]):
        self.screen = screen
        self.dim = dim
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])
        self.immagine = pygame.image.load("freccia.png")
        self.immagine = pygame.transform.scale(self.immagine, (self.rect.width, self.rect.height))
        self.screen.blit(self.immagine, (pos[0], pos[1]))
        self.velocità = [5,5]

    def muovi(self):
        self.rect.x += self.velocità[0]
        if self.rect.right >= self.screen.get_width():
            






        