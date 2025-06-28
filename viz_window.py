import pygame
import configs as cfg
import shapes
from buttons import viz_window_buttons

pygame.init()

def create_viz_window(surface_color):
    viz_window_surface = pygame.Surface((cfg.WIDTH, cfg.HEIGHT))
    viz_window_surface.fill(surface_color)

    for buttons in viz_window_buttons:
        buttons.draw(viz_window_surface)

    return viz_window_surface

def reset(surface, surface_color):
    surface.fill(surface_color)
