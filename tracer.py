import os

WINDOW_OFFSET = 80
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, WINDOW_OFFSET'
import pygame


pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

# Create a window with the current screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT-WINDOW_OFFSET))
pygame.display.set_caption("Tracer")

running = True

while running:
    # Event handling
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, BLACK, pos, 5)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(WHITE)
    
    pygame.display.update()