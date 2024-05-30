import pygame
#from miop import screen_height, screen, screen_width, bersaglio_speed_y


class Bersaglio:
    def __init__(self, screen) -> None:
        self.bersaglio = pygame.Rect(1800-200, 1500/2-75, 150, 150)
        self.colore = (255, 0, 0)
        self.screen = screen
        self.image = pygame.Surface((150,150))
    def draw(self):
        pygame.draw.rect(self.image, self.colore, self.bersaglio.get_rect())
        self.screen.blit(self.image, self.rect)
    def bersaglio_movement(self):
        self.bersaglio.y += bersaglio_speed_y
        if self.bersaglio.y <= 0 or self.bersaglio.y >= 1500:
            bersaglio_speed_y *= -1


