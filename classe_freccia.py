import pygame



class freccia:
    def _init_(self, screen,  dim = (30,30), pos = (0,0)):
        self.screen = screen
        self.dim = dim
        self.pos = pos
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])
        self.immagine = pygame.image.load("freccia.png")
        self.immagine = pygame.transform.scale(self.immagine, (self.rect.width, self.rect.height))
        self.screen.blit(self.immagine, (self.pos[0], self.pos[1]))
        self.velocità = [5,0]

    