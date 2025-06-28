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
SCREEN_HEIGHT = HEIGHT - WINDOW_OFFSET
screen = pygame.display.set_mode((WIDTH, SCREEN_HEIGHT))
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
font = pygame.font.SysFont("ubuntu", font_size)
text_offset = 5

# Shape Dimensions
line_width = 3
arrow_head_distance = 15

#Text Editor Dimensions
TEXT_EDITOR_WIDTH = WIDTH * 0.7

#Viz window dimensions
VIZ_WINDOW_WIDTH = WIDTH - TEXT_EDITOR_WIDTH
VIZ_WINDOW_HEIGHT = HEIGHT
VIZ_WINDOW_STARTING_X = 0

VIZ_WINDOW_STARTING_COORDINATES = (TEXTX)
