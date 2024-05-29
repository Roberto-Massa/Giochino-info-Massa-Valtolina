import pygame

screen_width = 1800
screen_height = 1500
screen = pygame.display.set_mode((screen_width,screen_height))

class Bersaglio:
    def __init__(self, pos = (30,30), dim = (30, 30)) -> None:
        self.bersaglio = pygame.Rect((pos[0], pos[1]), (dim[0], dim[1]))
        self.colore = (255,255,255)
    def draw(self):
        pygame.draw.ellipse(screen, self.colore, self.bersaglio)
    def bersaglio_movement(self):
        global bersaglio_speed_y 
        self.bersaglio.rect.y += bersaglio_speed_y
        if self.bersaglio.rect.y <= 0 or self.bersaglio.y >= screen_height:
            bersaglio_speed_y *= -1
        pass


        
    # def draw_bersaglio(self):
    #     pygame.draw.ellipse(screen, self.colore, self.bersaglio)
    # def movimento_bersaglio(self):
    #     global bersaglio_speed_y
        

        


