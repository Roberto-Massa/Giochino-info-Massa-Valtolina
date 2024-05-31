import pygame, sys
from pygame.locals import *
import math
from random import *

from classefreccia import Freccia
from bottone import Bottone
from bersaglio import Bersaglio
from punteggio import Punteggio



pygame.init()


#arciere in tensione


arciere_x1, arciere_y1, dim_arciere_x1, dim_arciere_y1 = 200, 90, 400, 450
rettangolo_arciere1 = pygame.Rect(arciere_x1, arciere_y1,dim_arciere_x1, dim_arciere_y1)
immagine_arciere1= pygame.image.load("egit1.png")
immagine_arciere1= pygame.transform.scale(immagine_arciere1, (rettangolo_arciere1.width, rettangolo_arciere1.height))


#arciere libero


arciere_x2, arciere_y2, dim_arciere_x2, dim_arciere_y2 = 200, 110, 450, 510
rettangolo_arciere2 = pygame.Rect(arciere_x2, arciere_y2,dim_arciere_x2, dim_arciere_y2)
immagine_arciere2= pygame.image.load("egit2.png")
immagine_arciere2= pygame.transform.scale(immagine_arciere2, (rettangolo_arciere2.width, rettangolo_arciere2.height))


#aereo 


aereo_x, aereo_y, dim_aereo_x, dim_aereo_y = 0, 300, 600, 400
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
nimmaginisfondo = math.ceil(larghezzaschermo/larghezzasfondo) + 1
scroll = 0



 

spawn_scritta = False
spawn_freccia = False
pausa = False
font = pygame.font.SysFont("Showcard Gothic", 60)
text = font.render("VITTORIA!!!", 1, (0, 0, 255))
        
sound_effect = pygame.mixer.Sound("indian-christmas.mp3")
sound_effect.set_volume(10)
sound_freccia = pygame.mixer.Sound("bow_shoot.mp3")
sound_freccia.set_volume(1)

bersaglio = Bersaglio(screen, 10)
freccia = Freccia(screen, (250,40), (330, 220))
bottone = Bottone(screen, (screen_width/2-200, screen_height/2+50), (400, 200), "RESET")
punteggio = Punteggio(screen, (20,20), (150,100))
npunteggio = 0


while True:

    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if spawn_freccia == False and spawn_scritta == False:
                sound_freccia.play()
            if pausa == False:
                spawn_freccia = True
                
            
            pos = pygame.mouse.get_pos()
            if spawn_scritta == True:
                if bottone.rect.collidepoint(pos):
                    sound_effect.stop()
                    spawn_scritta = False
                    pausa = False
                    freccia = Freccia(screen, (250,40), (330, 220))
                    velocitàbersagliocasuale = randint(2, 18)
                    bersaglio = Bersaglio(screen, velocitàbersagliocasuale)
                    

    #algoritmo sfondo   
                                
    for i in range(0, nimmaginisfondo):
        screen.blit(sfondo, (i * larghezzasfondo + scroll, 0))
    scroll -= 5
    if abs(scroll) > larghezzasfondo:
        scroll = 0

    
    screen.blit(immagine_aereo, (aereo_x, aereo_y))
    if spawn_freccia == False and pausa == False:
        screen.blit(immagine_arciere1, (arciere_x1, arciere_y1))
    if spawn_freccia == True or pausa == True:
        screen.blit(immagine_arciere2, (arciere_x2, arciere_y2))


    bersaglio.muovi()
    #punteggio.draw(npunteggio)
    if spawn_freccia == False and pausa == False:
        screen.blit(freccia.immagine, (330, 220))


    if spawn_freccia == True:
        freccia.draw()
        freccia.muovi()

    
    if freccia.rect.colliderect(bersaglio.rect):
        if freccia.rect.right < bersaglio.rect.x + bersaglio.rect.width/2:
            if spawn_freccia == True:
                sound_effect.play()
                npunteggio += 1
                punteggio.image.fill((0, 0, 0))
            spawn_freccia = False
            spawn_scritta = True

        
    if spawn_scritta == True:
        freccia.muoviconbersaglio(bersaglio.rect.y)
        screen.blit(text, (screen_width/2-180, screen_height/2-150))
        bottone.draw()
        pausa = True
    
    
    if freccia.rect.left>= screen.get_width():
        spawn_freccia = False
        freccia = Freccia(screen, (250,30), (330, 220))
        
        
    punteggio.draw(npunteggio)
    bersaglio.draw()
    

        
   
    clock.tick(fps)
    pygame.display.flip()
     
pygame.quit()
