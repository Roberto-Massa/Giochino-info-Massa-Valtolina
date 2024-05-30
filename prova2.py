import pygame
import math

# Inizializza Pygame
pygame.init()

# Imposta le dimensioni della finestra
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Angry Birds Clone")

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Carica le immagini
bird_image = pygame.image.load("rape.jpg")  # Dovresti avere un'immagine "bird.png"
bird_image = pygame.transform.scale(bird_image, (250, 250))
bird_rect = bird_image.get_rect(center=(100, screen_height - 100))

# Variabili del gioco
clock = pygame.time.Clock()
running = True
launching = False
gravity = 0.5
bird_pos = [100, screen_height - 100]
bird_vel = [0, 0]

# Definisce gli ostacoli
obstacles = [
    pygame.Rect(400, screen_height - 50, 50, 50),
    pygame.Rect(500, screen_height - 100, 50, 100),
    pygame.Rect(600, screen_height - 150, 50, 150)
]

# Funzione per il disegno della fionda
def draw_sling():
    pygame.draw.line(screen, BLACK, (100, screen_height - 100), bird_pos, 5)

# Loop principale del gioco
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not launching:
            bird_pos = list(pygame.mouse.get_pos())
            bird_vel = [0, 0]
        elif event.type == pygame.MOUSEBUTTONUP and not launching:
            if math.hypot(bird_pos[0] - 100, bird_pos[1] - (screen_height - 100)) > 10:
                launching = True
                bird_vel = [-(bird_pos[0] - 100) * 0.1, -(bird_pos[1] - (screen_height - 100)) * 0.1]

    if launching:
        bird_vel[1] += gravity
        bird_pos[0] += bird_vel[0]
        bird_pos[1] += bird_vel[1]

        if bird_pos[1] > screen_height - bird_rect.height:
            bird_pos[1] = screen_height - bird_rect.height
            bird_vel[1] *= -0.5  # Rimbalzo

        # Controlla le collisioni con gli ostacoli
        bird_rect.center = bird_pos
        for obstacle in obstacles[:]:
            if bird_rect.colliderect(obstacle):
                obstacles.remove(obstacle)

    # Riempie lo schermo di bianco
    screen.fill(WHITE)

    # Disegna la fionda
    if not launching:
        draw_sling()

    # Disegna l'uccello
    bird_rect.center = bird_pos
    screen.blit(bird_image, bird_rect)

    # Disegna gli ostacoli
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, obstacle)

    # Aggiorna lo schermo
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

pygame.quit()
