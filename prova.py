import pygame
import math
import sys

# Inizializza Pygame
pygame.init()

# Imposta le dimensioni della finestra
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gioco dell'arciere")

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
FPS = 60
VEL_FRECCIA = 0.2

# Funzioni per disegnare l'arciere, la freccia e il bersaglio
def draw_archer(surface, x, y):
    pygame.draw.rect(surface, BROWN, (x, y, 20, 60))  # Corpo
    pygame.draw.line(surface, BROWN, (x+10, y+30), (x+30, y+10), 5)  # Arco
    pygame.draw.line(surface, BLACK, (x+10, y+30), (x+30, y+50), 2)  # Cordicella

def draw_arrow(surface, x, y, angle):
    arrow_length = 50
    end_x = x + arrow_length * math.cos(math.radians(angle))
    end_y = y - arrow_length * math.sin(math.radians(angle))
    pygame.draw.line(surface, BLACK, (x, y), (end_x, end_y), 5)  # Freccia

def draw_target(surface, x, y):
    pygame.draw.circle(surface, RED, (x, y), 30)  # Cerchio esterno
    pygame.draw.circle(surface, WHITE, (x, y), 20)  # Cerchio intermedio
    pygame.draw.circle(surface, RED, (x, y), 10)  # Cerchio interno

# Posizioni iniziali
archer_x = 50
archer_y = screen_height // 2 - 30
target_x = screen_width - 100
target_y = screen_height // 2

# Freccia
arrow_speed = 0
arrow_angle = 0
arrow_x = archer_x + 30
arrow_y = archer_y + 30
arrow_flying = False

# Funzione per disegnare tutto
def draw():
    screen.fill(WHITE)
    draw_archer(screen, archer_x, archer_y)
    draw_target(screen, target_x, target_y)
    if arrow_flying:
        draw_arrow(screen, arrow_x, arrow_y, arrow_angle)
    pygame.display.flip()

# Loop principale del gioco
running = True
clock = pygame.time.Clock()
tempo_premuto = 0
conta = 0
velocita_freccia_iniziale = 5

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not arrow_flying:
                arrow_speed = 0
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if not arrow_flying:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                arrow_angle = math.degrees(math.atan2(mouse_y - arrow_y, mouse_x - arrow_x))
                arrow_speed = 15  # Puoi modificare la velocità
                arrow_flying = True
        
        mouse_pressed = pygame.mouse.get_pressed() # (True, False, False)
        if mouse_pressed[0] == True:
            if tempo_premuto == 0:
                tempo_premuto = tempo
                arrow_speed = velocita_freccia_iniziale
            if arrow_speed < 20:
                arrow_speed += VEL_FRECCIA
            tempo_premuto += 1
        else:
            tempo_premuto = 0
        conta += 1
        tempo = conta / FPS   

    if arrow_flying:
        arrow_x += arrow_speed * math.cos(math.radians(arrow_angle))
        arrow_y -= arrow_speed * math.sin(math.radians(arrow_angle))

        if arrow_x > screen_width or arrow_y < 0 or arrow_y > screen_height:
            arrow_flying = False
            arrow_x = archer_x + 30
            arrow_y = archer_y + 30
    


    draw()
    clock.tick(60)

pygame.quit()
sys.exit()