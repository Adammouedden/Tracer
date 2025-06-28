import pygame
import shapes
import configs as cfg


def create_text_window():
    text_window = pygame.Surface((cfg.WIDTH, cfg.TEXT_WINDOW_HEIGHT))
    return text_window
