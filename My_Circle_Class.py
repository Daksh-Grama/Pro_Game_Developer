import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
screen.fill(WHITE)

class Circle():
    def __init__(self, color, pos, rad, WID = 0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.WID = WID
        self.screen = screen
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.rad, self.WID)
    
    def grow(self, x):
        self.rad += x
        pygame.draw.circle(self.screen, self.color, self.pos, self.rad, self.WID)

position = (300, 300)
radius = 50
WID = 2
pygame.draw.circle(screen, RED, position, radius, WID)
pygame.display.update()        

#creating instances
blue_circle = Circle(BLUE, position, radius + 60)
red_circle = Circle(RED, position, radius + 40)
yellow_circle = Circle(YELLOW, position, radius, 5)
green_circle = Circle(GREEN, position, 20)

running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            blue_circle.draw()
            red_circle.draw()
            yellow_circle.draw()
            green_circle.draw()
            pygame.display.update()

        elif (event.type == pygame.MOUSEBUTTONUP):
            blue_circle.grow(2)
            red_circle.grow(2)
            yellow_circle.grow(2)
            green_circle.grow(2)
            pygame.display.update()
    
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            black_circle = Circle(BLACK, pos, 5)
            black_circle.draw()
            pygame.display.update()

