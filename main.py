import pygame, sys
from pygame.locals import *
import math

from classefreccia import Freccia
from bottone import Bottone
from Bersaglio import Bersaglio



pygame.init()


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
nimmaginisfondo = math.ceil(larghezzaschermo/larghezzasfondo) + 1
scroll = 0
arciere = pygame.image.load("arciere.png").convert()


 

     




spawn_scritta = False
spawn_freccia = False
pausa = False
font = pygame.font.Font(None, 50)
text = font.render("VITTORIA!!!", 1, (0, 0, 255))
        
sound_effect = pygame.mixer.Sound("right-foot-creep.mp3")
sound_effect.set_volume(0.2)
sound_effect
suondcounter = 0
bersaglio = Bersaglio(screen)
freccia = Freccia(screen, (250,40), (400, 120))
bottone = Bottone(screen, (screen_width/2-200, screen_height/2+50), (400, 200), "RESET")


while True:

    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pausa == False:
                spawn_freccia = True
            
            pos = pygame.mouse.get_pos()
            if spawn_scritta == True:
                if bottone.rect.collidepoint(pos):
                    spawn_scritta = False
                    
                    pausa = False
                    freccia = Freccia(screen, (250,40), (400, 120))
                    

    #algoritmo sfondo   
                                  
    for i in range(0, nimmaginisfondo):
        screen.blit(sfondo, (i * larghezzasfondo + scroll, 0))
    scroll -= 5
    if abs(scroll) > larghezzasfondo:
        scroll = 0

    
    screen.blit(immagine_aereo, (aereo_x, aereo_y))
    screen.blit(immagine_arciere, (arciere_x, arciere_y))

    bersaglio.muovi()
    if spawn_freccia == True:
        freccia.draw()
        freccia.muovi()



    if freccia.rect.colliderect(bersaglio.rect):
        sound_effect.play(loops=0)
        
        spawn_freccia = False
        spawn_scritta = True
        

    

    if spawn_scritta == True:
        freccia.muoviconbersaglio(bersaglio.rect.y)
        screen.blit(text, (screen_width/2-50, screen_height/2))
        bottone.draw()
        pausa = True
    
    
    
    if freccia.rect.right >= screen.get_width():
        spawn_freccia = False
        freccia = Freccia(screen, (250,30), (400, 120))
        
        

    bersaglio.draw()
    

        
    suondcounter += 1
    clock.tick(fps)
    pygame.display.flip()
    
pygame.quit()
