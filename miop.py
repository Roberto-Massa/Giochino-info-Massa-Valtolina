import pygame, sys
from pygame.locals import *
import math

from classefreccia import freccia
from classereset import bottone

pygame.init()

freccia_x, freccia_y, dim_freccia_x, dim_freccia_y = 300, 150, 200, 50
rettangolo_freccia = pygame.Rect(freccia_x, freccia_y, dim_freccia_x, dim_freccia_y)
immagine_freccia = pygame.image.load("freccia.png")
immagine_freccia = pygame.transform.scale(immagine_freccia, (rettangolo_freccia.width, rettangolo_freccia.height))


arciere_x, arciere_y, dim_arciere_x, dim_arciere_y = 200, 0, 300, 450
rettangolo_arciere = pygame.Rect(arciere_x, arciere_y,dim_arciere_x, dim_arciere_y)
immagine_arciere= pygame.image.load("arciere3.png")
immagine_arciere= pygame.transform.scale(immagine_arciere, (rettangolo_arciere.width, rettangolo_arciere.height))


aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 0, 250, 600, 400
rettangolo_aereo= pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
immagine_aereo = pygame.image.load("aereo.png")
immagine_aereo = pygame.transform.scale(immagine_aereo, (rettangolo_aereo.width, rettangolo_aereo.height))

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
        


# def movimento():
#     global x
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.MOUSEBUTTONDOWN]:
#         x = x+3
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
arciere = pygame.image.load("arciere3.png").convert()





arrow_flying = False
freccia_velocità = 0
freccia_angolo = 0

#variabilitempopremuto
tempo_iniziale = 0
velocità = 0
aumento_velocità = 5
massimo_tempo = 5 

freccia_ = freccia(screen, (200, 50), (300, 150))
reset = bottone(screen, (screen_width/2-100, screen_height/2-50), (200, 100), "RESET")



while True:
    clock.tick(fps)

    

    #algoritmo sfondo
    for i in range(0, nimmagini):
        screen.blit(sfondo, (i * larghezzasfondo + scroll, 0))
    scroll -= 5
    if abs(scroll) > larghezzasfondo:
        scroll = 0
    
    screen.blit(immagine_aereo, (aereo_x, aereo_y))
    screen.blit(immagine_arciere, (arciere_x, arciere_y))

    
    
  
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            freccia_.muovi
            if freccia_.rect.right >= screen.get_width():
                reset.draw()

            
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if not arrow_flying:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                freccia_angolo = math.degrees(math.atan2(mouse_y - freccia_y, mouse_x - freccia_x))
                freccia_velocità = velocità  
                arrow_flying = True

            
        if tempo_iniziale:
            tempo_trascorso = (pygame.time.get_ticks() - tempo_iniziale) / 1000
            if tempo_trascorso <= massimo_tempo:
                velocità = aumento_velocità * int(tempo_trascorso)
            if tempo_trascorso > massimo_tempo:
                velocità = aumento_velocità * massimo_tempo
        
        if arrow_flying:
            freccia_x += freccia_velocità * math.cos(math.radians(freccia_angolo))
            freccia_y -= freccia_velocità * math.sin(math.radians(freccia_angolo)) 

        if freccia_x > WINDOW_SIZE[0] or freccia_y < 0 or freccia_y > WINDOW_SIZE[1]:
                arrow_flying = False
                arrow_x = 300
                arrow_y = 150
                velocità = 0

        screen.blit(immagine_freccia, (freccia_x, freccia_y))
    
    pygame.display.update()
    # pygame.display.flip()
    
pygame.quit()
