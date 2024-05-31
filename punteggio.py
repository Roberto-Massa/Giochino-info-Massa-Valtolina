import pygame
class Punteggio:
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.pos = pos
        self.size = pos
        self.image = pygame.Surface(size)
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        

    def draw(self, testo):
        font = pygame.font.Font(None, 50)
        text = font.render(str(testo), 1, (0, 0, 255))
        x = self.rect.width / 2 - text.get_width() / 2
        y = self.rect.height / 2 - text.get_height() / 2
        self.image.blit(text, (x,y))
        self.screen.blit(self.image, (self.pos))
        