import pygame
from miop import screen_height, screen, screen_width, bersaglio_speed_y


class Bersaglio:
    def __init__(self) -> None:
        self.bersaglio = pygame.Rect((screen_width-200, screen_height/2-75), (150, 150))
        self.colore = (255, 0, 0)
    def draw(self):
        pygame.draw.rect(screen, self.colore, self.bersaglio)
        pass
    def bersaglio_movement(self):
        self.bersaglio.y += bersaglio_speed_y
        if self.bersaglio.y <= 0 or self.bersaglio.y >= screen_height:
            bersaglio_speed_y *= -1


