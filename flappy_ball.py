import pgzrun
from random import randint

TITLE = "Flappy Ball Game!" 
WIDTH = 800
HEIGHT = 600

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)

color = R, G, B
gravity = 2000.0

class Ball:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, color)

ball = Ball(50, 100)

def draw():
    screen.clear()
    ball.draw()

def update(dt):
    #apply constant acceleration formula
    uy = ball.vy
    ball.vy += gravity*dt
    ball.y += (uy + ball.vy) *0.5*dt

    #detect and handle bounce
    if ball.y > HEIGHT - ball.radius: #the ball has bounced
        ball.y = HEIGHT - ball.radius # fixing the position of the ball
        ball.vy = -ball.vy*0.9

    #x component does not have acceleration
    ball.x += ball.vx*dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    #pressin a key will make the ball go upwards
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()