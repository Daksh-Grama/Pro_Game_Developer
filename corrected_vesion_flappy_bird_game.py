import pygame
import random

# Initialize
pygame.init()
clock = pygame.time.Clock()
fps = 60

# Screen
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Game Variables
gravity = 0.5
bird_movement = 0
game_active = False
game_over = False
score = 0
high_score = 0
pipe_spawn_time = 1200
pipe_gap = 150
scroll_speed = 4

# Load Images
bg = pygame.image.load("background.png").convert()
ground = pygame.image.load("ground.png").convert()
bird_frames = [pygame.image.load(f"bird{i}.png").convert_alpha() for i in range(1, 4)]
pipe_image = pygame.image.load("pipe.png").convert_alpha()
restart_img = pygame.image.load("restart.png").convert_alpha()

# Bird
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, screen_height//2))
bird_anim_counter = 0

# Pipes
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, pipe_spawn_time)

# Font
font = pygame.font.SysFont('Arial', 40)

# Restart Button
restart_rect = restart_img.get_rect(center=(screen_width // 2, screen_height // 2))


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= screen_height:
            screen.blit(pipe_image, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_image, False, True)
            screen.blit(flip_pipe, pipe)


def create_pipe():
    height = random.randint(200, 400)
    bottom_pipe = pipe_image.get_rect(midtop=(screen_width + 50, height))
    top_pipe = pipe_image.get_rect(midbottom=(screen_width + 50, height - pipe_gap))
    return bottom_pipe, top_pipe


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 550:
        return False
    return True


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def display_score(game_state):
    if game_state == 'main':
        score_surface = font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(screen_width / 2, 50))
        screen.blit(score_surface, score_rect)
    if game_state == 'over':
        score_surface = font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(screen_width / 2, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(screen_width / 2, 100))
        screen.blit(high_score_surface, high_score_rect)


# Main Game Loop
running = True
while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_movement = -10
                game_active = True
            if event.key == pygame.K_SPACE and game_over:
                pipe_list.clear()
                bird_rect.center = (100, screen_height // 2)
                bird_movement = 0
                score = 0
                game_active = False
                game_over = False

        if event.type == SPAWNPIPE and game_active:
            pipe_list.extend(create_pipe())

    if game_active:
        # Bird
        bird_movement += gravity
        bird_rect.centery += int(bird_movement)

        bird_anim_counter += 1
        if bird_anim_counter % 5 == 0:
            bird_index = (bird_index + 1) % len(bird_frames)
        bird_surface = bird_frames[bird_index]
        rotated_bird = pygame.transform.rotate(bird_surface, -bird_movement * 3)
        screen.blit(rotated_bird, bird_rect)

        # Pipes
        pipe_list = [pipe.move(-scroll_speed, 0) for pipe in pipe_list]
        draw_pipes(pipe_list)

        # Collision
        game_active = check_collision(pipe_list)
        if not game_active:
            game_over = True

        # Score
        for pipe in pipe_list:
            if pipe.centerx == bird_rect.centerx:
                score += 100  # Two pipes per set
    else:
        if game_over:
            screen.blit(restart_img, restart_rect)
        else:
            screen.blit(bird_surface, bird_rect)

    # Ground
    screen.blit(ground, (0, 550))

    # Display score
    if not game_over:
        display_score('main')
    else:
        high_score = update_score(score, high_score)
        display_score('over')

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
