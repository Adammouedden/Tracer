import pygame
import configs as cfg
import shapes
from buttons import viz_window_buttons

pygame.init()

def create_viz_window(surface_color):
    viz_window_surface = pygame.Surface((cfg.WIDTH, cfg.HEIGHT))
    viz_window_surface.fill(surface_color)


    return viz_window_surface

def reset(surface, surface_color):
    surface.fill(surface_color)

def draw_viz_buttons(surface):
    for buttons in viz_window_buttons:
        buttons.draw(surface)
