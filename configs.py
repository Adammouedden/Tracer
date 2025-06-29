import pygame
import sys

# Pygame Initialization
pygame.init()

# Screen Variables
screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
WINDOW_OFFSET = 80
FPS = sys.maxsize  # Set FPS to maximum possible value

screen = pygame.display.set_mode((WIDTH, HEIGHT - WINDOW_OFFSET))
pygame.display.set_caption("Tracer") # Set the window title

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
HIGHLIGHT_YELLOW = (255, 255, 0, 100)
HIGHLIGHT_RED = (255, 0, 0, 100)

# Fonts
font_size = 100
font = pygame.font.SysFont("ubuntu", font_size)
text_offset = 5

# Button sizing
button_width = 50
button_height = 50 
button_spacing = 60 
button_margin = 15

# Shape Dimensions
line_width = 3
arrow_head_distance = 15

#Text Editor Dimensions
TEXT_EDITOR_WIDTH = WIDTH * 0.3
TEXT_EDITOR_WIDTH = WIDTH * 0.3

#Viz window dimensions
VIZ_WINDOW_WIDTH = WIDTH - TEXT_EDITOR_WIDTH
VIZ_WINDOW_HEIGHT = int((HEIGHT - WINDOW_OFFSET) * 0.7)


VIZ_WINDOW_STARTING_X = TEXT_EDITOR_WIDTH
VIZ_WINDOW_STARTING_Y = 0

VIZ_WINDOW_STARTING_COORDINATES = (VIZ_WINDOW_STARTING_X, VIZ_WINDOW_STARTING_Y)
TEXT_WINDOW_HEIGHT = (HEIGHT - WINDOW_OFFSET) - VIZ_WINDOW_HEIGHT
