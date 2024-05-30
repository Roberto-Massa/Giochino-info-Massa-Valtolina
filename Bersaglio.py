import pygame
#from miop import screen_height, screen, screen_width, bersaglio_speed_y


class Bersaglio:
    def __init__(self, screen) -> None:
        self.bersaglio = pygame.Rect(1500-200, 600/2-75, 44, 100)
        self.colore = (245, 65, 89)
        self.screen = screen
        self.image = pygame.Surface((150,150))
    def draw(self):
        pygame.draw.rect(self.image, self.colore, self.image.get_rect())
        self.screen.blit(self.image, self.bersaglio)
    def bersaglio_movement(self):
        self.bersaglio.y += bersaglio_speed_y
        if self.bersaglio.y <= 0 or self.bersaglio.y >= 1500:
            bersaglio_speed_y *= -1


