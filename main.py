import pygame, sys
from pygame.locals import *
import math

from classefreccia import Freccia
from bottone import Bottone
from Bersaglio import Bersaglio






pygame.init()
# freccia_speed_x = 5
# freccia_x, freccia_y, dim_freccia_x, dim_freccia_y = 300, 150, 200, 50
# rettangolo_freccia = pygame.Rect(freccia_x, freccia_y, dim_freccia_x, dim_freccia_y)
# immagine_freccia = pygame.image.load("freccia.png")
# immagine_freccia = pygame.transform.scale(immagine_freccia, (rettangolo_freccia.width, rettangolo_freccia.height))

#arciere



arciere_x, arciere_y, dim_arciere_x, dim_arciere_y = 200, 0, 300, 450
rettangolo_arciere = pygame.Rect(arciere_x, arciere_y,dim_arciere_x, dim_arciere_y)
immagine_arciere= pygame.image.load("arciere.png")
immagine_arciere= pygame.transform.scale(immagine_arciere, (rettangolo_arciere.width, rettangolo_arciere.height))

#aereo 

aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 0, 250, 600, 400
rettangolo_aereo= pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
immagine_aereo = pygame.image.load("aereo.png")
immagine_aereo = pygame.transform.scale(immagine_aereo, (rettangolo_aereo.width, rettangolo_aereo.height))


screen_height = 600
screen_width = 1500
WINDOW_SIZE = (1500, 600)
larghezzaschermo = WINDOW_SIZE[0]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption('Gioco arciere')

# clock per temporizzare il programma
clock = pygame.time.Clock()
fps = 60

sfondo = pygame.image.load("sfondo.jpg").convert()
sfondo = pygame.transform.scale(sfondo, (1500, 600))
larghezzasfondo = sfondo.get_width()
nimmagini = math.ceil(larghezzaschermo/larghezzasfondo) + 1
scroll = 0
arciere = pygame.image.load("arciere.png").convert()

def freccia_stop():
    global freccia_speed_x
    freccia_speed_x = 0
    return freccia_speed_x 

     




scritta = False
spawn_freccia = False
font = pygame.font.Font(None, 50)
text = font.render("hai vinto", 1, (255, 0, 0))
        

bersaglio = Bersaglio(screen)
colore_bersaglio = (0,0,0)
freccia = Freccia(screen, (250,100), (50, 100))

bottone = Bottone(screen, (screen_width/2-100, screen_height/2-50), (200, 100), "RESET")


while True:

    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            spawn_freccia = True
            
            pos = pygame.mouse.get_pos()
            if scritta == True:
                if bottone.rect.collidepoint(pos):
                    scritta = False
            
            

    # if freccia.rect.colliderect(bersaglio):
    #     freccia_stop()
    #     scritta = True
    # if scritta == True:
    #     screen.blit(text(720, 200))
    #     bottone.draw()
    
    
         

    # if freccia.rect.right >= screen.get_width():
    #     reset.draw()
                

    #algoritmo sfondo                 
    for i in range(0, nimmagini):
        screen.blit(sfondo, (i * larghezzasfondo + scroll, 0))
    scroll -= 5
    if abs(scroll) > larghezzasfondo:
        scroll = 0
    
    screen.blit(immagine_aereo, (aereo_x, aereo_y))
    screen.blit(immagine_arciere, (arciere_x, arciere_y))

    bersaglio.draw()
    if spawn_freccia == True:
        freccia.draw()

        
    
    clock.tick(fps)
    pygame.display.flip()
    
pygame.quit()
