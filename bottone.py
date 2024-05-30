import pygame
white = (255, 255, 255)
class Bottone:
    def __init__(self, screen, pos, size, testo) -> None:
        self.screen = screen
        self.pos = pos
        self.size = size
        self.testo = testo
        self.colore = (0, 255, 255)
        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.font = pygame.font.Font(None, 50)
        

    def draw(self):
        self.image.fill(white)
        self.text = self.font.render(self.testo, 1, self.colore)
        pygame.draw.rect(self.image, (self.colore), (0, 0, self.rect.width, self.rect.height), 5)
        x = self.rect.width / 2 - self.text.get_width() / 2
        y = self.rect.height / 2 - self.text.get_height() / 2
        self.image.blit(self.text, (x, y))
        self.screen.blit(self.image, self.rect)