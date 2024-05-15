import pygame, sys
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption('Disegni e click')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60
colore = (255,0,0)
colore4 = (180,189,78)
screen.fill(colore4)
colore2 = (0,160,0)
colore3 = (255, 255, 255)
pygame.draw.rect(screen, colore, (330,190,20,20))
pygame.draw.rect(screen, colore2, (300,190,20,20))
pygame.draw.rect(screen, colore3, (315,100,20,90))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
    
