import pygame
import configs as cfg
import shapes

pygame.init()

def create_viz_window(surface_color):
    viz_window_surface = pygame.Surface((cfg.WIDTH, cfg.HEIGHT))
    viz_window_surface.fill(surface_color)
    return viz_window_surface

def reset(surface, surface_color):
    surface.fill(surface_color)


