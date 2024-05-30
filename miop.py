import pygame, sys
from pygame.locals import *
import math
<<<<<<< HEAD
=======
from class_Bersaglio import Bersaglio
>>>>>>> ca80924094846d272664b8df549f264f17333f7b

pygame.init()

WINDOW_SIZE = (1500, 600)
larghezzaschermo = 1500
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption('Disegni e click')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

sfondo = pygame.image.load("sfondo.jpg").convert()
sfondo = pygame.transform.scale(sfondo, (1500, 600))
larghezzasfondo = sfondo.get_width()
nimmagini = math.ceil(screen_width/larghezzasfondo) + 1
scroll = 0
<<<<<<< HEAD
=======
arcere = pygame.image.load("yaa.jpg").convert()
bersaglio = Bersaglio(screen)
>>>>>>> ca80924094846d272664b8df549f264f17333f7b

while True:
      
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    

    

    #algoritmo sfondo
    for i in range(0, nimmagini):
        screen.blit(sfondo, (i * larghezzasfondo + scroll, 0))
    scroll -= 5
    if abs(scroll) > larghezzasfondo:
        scroll = 0

    rettangolino1 = pygame.draw.rect(screen, colore, (330,190,20,20))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
pygame.quit()
