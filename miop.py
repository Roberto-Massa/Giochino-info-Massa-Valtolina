import pygame, sys
from pygame.locals import *
import math
from class_Bersaglio import Bersaglio

pygame.init()









screen_width = 1800
screen_height = 1500
screen = pygame.display.set_mode((screen_width,screen_height))
bersaglio_speed_y = 5
pygame.display.set_caption('Disegni e click')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60
colore = (255,0,0)







# screen.fill(colore4)
# colore2 = (0,160,0)
# colore3 = (255, 255, 255)
# pygame.draw.rect(screen, colore, (330,190,20,20))
# pygame.draw.rect(screen, colore2, (300,190,20,20))
# pygame.draw.rect(screen, colore3, (315,100,20,90))


sfondo = pygame.image.load("yaa.jpg").convert()
larghezzasfondo = sfondo.get_width()
nimmagini = math.ceil(screen_width/larghezzasfondo) + 1
scroll = 0
arcere = pygame.image.load("yaa.jpg").convert()
bersaglio = Bersaglio(screen)

while True:
      
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    

    for i in range(0, nimmagini):
        screen.blit(sfondo, (i * larghezzasfondo + scroll, 0))

    scroll -= 5
    if abs(scroll) > larghezzasfondo:
        scroll = 0
    bersaglio.draw()
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
