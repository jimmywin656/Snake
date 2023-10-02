import pygame
import time
import random

snake_speed = 12

# Window size
window_x = 400
window_y = 300

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Initialize game window
pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Define snake default position
snake_position = [100, 50]

# Define first 4 blocks of snake body
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# Setting default snake direction towards right
direction = "RIGHT"
change_to = direction

# Initial score
score = 0

# game variable
running = True

# displaying Score function
def show_score (score):
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, white)
    game_window.blit(score_text, (10, 10))

# game over function
def game_over():
    # create font object
    my_font = pygame.font.SysFont('times new roman', 50)

    # create a text surface on which text will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)

    # create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    # set position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Wait for a few seconds to display the game over screen
    pygame.time.delay(2000)  # Delay for 2000 milliseconds (2 seconds)

    # Deactivate the font system before quitting Pygame
    pygame.font.quit()
    pygame.quit()

# Main game loop
while running:
    # if user clicks X to exit program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        change_to = 'UP'
    if keys[pygame.K_DOWN]:
        change_to = 'DOWN'
    if keys[pygame.K_LEFT]:
        change_to = 'LEFT'
    if keys[pygame.K_RIGHT]:
        change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake growing mechanic
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0],  pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
        running = False
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
        running = False

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
            running = False

    # displaying score continuously
    if running:
        show_score(score)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second / Refresh Rate
        fps.tick(snake_speed)