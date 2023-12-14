
"""
Jack Davis
Final Project

"""

import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
GOAL_WIDTH, GOAL_HEIGHT = 200, 100
GOALIE_WIDTH, GOALIE_HEIGHT = 100, 50
BALL_RADIUS = 20
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goalie Game")


clock = pygame.time.Clock()


score = 0
game_start_time = pygame.time.get_ticks()
game_duration = 60 * 1000  # 1 minute in milliseconds
last_ball_time = pygame.time.get_ticks()


goalie_x = (WIDTH - GOALIE_WIDTH) // 2
goalie_y = HEIGHT - GOALIE_HEIGHT - 20
goalie_speed = 5


ball_x = 0
ball_y = 0
ball_speed = 5
ball_directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]

def draw_goalie(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, GOALIE_WIDTH, GOALIE_HEIGHT])

def draw_goal():
    pygame.draw.rect(screen, WHITE, [(WIDTH - GOAL_WIDTH) // 2, HEIGHT - GOAL_HEIGHT, GOAL_WIDTH, GOAL_HEIGHT])

def draw_ball(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), BALL_RADIUS)

def reset_ball():
    global ball_x, ball_y
    ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
    ball_y = random.randint(BALL_RADIUS, HEIGHT // 2)

def check_goalie_collision():
    return goalie_x < ball_x + BALL_RADIUS < goalie_x + GOALIE_WIDTH and goalie_y < ball_y + BALL_RADIUS < goalie_y + GOALIE_HEIGHT


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    elapsed_time = pygame.time.get_ticks() - game_start_time

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and goalie_x > 0:
        goalie_x -= goalie_speed
    if keys[pygame.K_RIGHT] and goalie_x < WIDTH - GOALIE_WIDTH:
        goalie_x += goalie_speed

    
    if pygame.time.get_ticks() - last_ball_time > 5000:  # 5000 milliseconds = 5 seconds
        ball_direction = random.choice(ball_directions)
        ball_x += ball_direction[0] * ball_speed
        ball_y += ball_direction[1] * ball_speed
        last_ball_time = pygame.time.get_ticks()

    
    if check_goalie_collision():
        score += 1
        reset_ball()

    
    screen.fill(BLACK)
    draw_goal()
    draw_goalie(goalie_x, goalie_y)
    draw_ball(ball_x, ball_y)

    
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

   
    time_left = max(0, int((game_duration - elapsed_time) / 1000))
    timer_text = font.render("Time: " + str(time_left) + "s", True, WHITE)
    screen.blit(timer_text, (WIDTH - 150, 10))

    pygame.display.flip()

    
    if elapsed_time >= game_duration:
        pygame.time.delay(2000)  
        pygame.quit()
        sys.exit()

    clock.tick(FPS)
 