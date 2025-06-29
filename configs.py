import pygame
import sys

# Pygame Initialization
pygame.init()

# Screen Variables
screen_info = pygame.display.Info()
WINDOW_OFFSET = 80
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h

FPS = 60  # Set FPS to maximum possible value

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

#VISUAL STUDIO COLORS
VS_GREY = (31, 31, 31)
VS_LIGHT_GREY = (67, 67, 67)
VS_BLACK = (24, 24, 24)
VS_OFF_WHITE = (172, 172, 172)
VS_LIGHTBLUE = (61, 144, 228)

HIGHLIGHT_YELLOW = (255, 255, 0, 100)
HIGHLIGHT_RED = (255, 0, 0, 100)


# Fonts
font_size = 100
font = pygame.font.SysFont("Ubuntu", font_size)
#font = pygame.font.Font("C:/Windows/Fonts/consola.ttf", font_size)
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

#Viz window dimensions
VIZ_WINDOW_WIDTH = WIDTH - TEXT_EDITOR_WIDTH
VIZ_WINDOW_HEIGHT = int((HEIGHT - WINDOW_OFFSET) * 0.9)

VIZ_WINDOW_STARTING_X = TEXT_EDITOR_WIDTH
VIZ_WINDOW_STARTING_Y = 0

VIZ_WINDOW_STARTING_COORDINATES = (VIZ_WINDOW_STARTING_X, VIZ_WINDOW_STARTING_Y)
TEXT_WINDOW_HEIGHT = (HEIGHT - WINDOW_OFFSET) - VIZ_WINDOW_HEIGHT
