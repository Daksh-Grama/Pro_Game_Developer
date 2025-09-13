import pygame
from pygame.locals import *
import random


pygame.init()
clock = pygame.time.Clock()
fps = 72

screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

font = pygame.font.SysFont("Algerian", 60)
white  = (255, 255, 255)
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 200
pipe_frequency = 2500 #miliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

#load images
Background = pygame.image.load("C:/Users/daksh/My Drive/Daksh Jetlearn Work/Pro_Game_Developer/images/bggground.png")
Ground = pygame.image.load("C:/Users/daksh/My Drive/Daksh Jetlearn Work/Pro_Game_Developer/images/ground.png")
Restart = pygame.image.load("C:/Users/daksh/My Drive/Daksh Jetlearn Work/Pro_Game_Developer/images/restart.png")
#Pipe = pygame.image.load("C:/Users/daksh/My Drive/Daksh Jetlearn Work/Pro_Game_Developer/images/pipe.png")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height/2)
    score = 0 
    return score




