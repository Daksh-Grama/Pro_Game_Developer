import pygame
pygame.init()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((600, 600))
screen.fill(BLACK)
pygame.display.update()

class rectangle():
    def __init__(self, color, dimensions):
        self.rect_surf = screen
        self.rect_dimensions = dimensions
        self.rect_color = color

    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

RED_rect = rectangle(RED, (50, 20, 120, 75))
GREEN_rect = rectangle(GREEN, (150, 200, 175, 100))
BLUE_rect = rectangle(BLUE, (300, 400, 200, 120))

RED_rect.draw()
GREEN_rect.draw()
BLUE_rect.draw()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
