import pygame
import configs as cfg
import shapes

pygame.init()

def create_viz_window(surface_color):
    viz_window_surface = pygame.Surface((cfg.VIZ_WINDOW_WIDTH, cfg.VIZ_WINDOW_HEIGHT))
    viz_window_surface.fill(surface_color)
    shapes.draw_line(viz_window_surface, (cfg.VIZ_WINDOW_WIDTH//2, 0), (cfg.VIZ_WINDOW_WIDTH//2, cfg.VIZ_WINDOW_HEIGHT))
    return viz_window_surface

def reset(surface, surface_color):
    surface.fill(surface_color)