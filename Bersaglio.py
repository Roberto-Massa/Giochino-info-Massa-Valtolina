import pygame
#from miop import screen_height, screen, screen_width, bersaglio_speed_y

window = [1500,600]
class Bersaglio:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.colore = (245, 65, 89)
        self.rect = pygame.Rect(1500-200, 600/2-75, 100, 100)
        self.immagine = pygame.image.load("bersagliotagliato.png")
        self.immagine = pygame.transform.scale(self.immagine, (self.rect.width, self.rect.height))
        self.velocità_y = 8
    def draw(self):
        # pygame.draw.rect(self.immagine, self.colore, self.immagine.get_rect())
        self.screen.blit(self.immagine, self.rect)
    def muovi(self):
        self.rect.y += self.velocità_y
        if self.rect.y <= 0 + 30  or  self.rect.bottom >= window[1] - 30:
            self.velocità_y  = self.velocità_y*-1


