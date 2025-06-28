import os
import pygame

# Pygame Initialization
pygame.init()

# Screen Variables
screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
WINDOW_OFFSET = 80
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, WINDOW_OFFSET'
screen = pygame.display.set_mode((WIDTH, HEIGHT-WINDOW_OFFSET))
pygame.display.set_caption("Tracer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
HIGHLIGHT = (255, 255, 0, 100)

# Fonts
font_size = 100
font = pygame.font.Font("ubuntu", font_size)
text_offset = 5