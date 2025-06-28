import pygame
import configs as cfg

pygame.init()

#Base Shapes
def draw_text(surface, text: str, coordinates, font_size = 20, color = cfg.BLACK):
    font = pygame.font.SysFont("ubuntu", font_size)
    #text_surface = font.render(text, True, color) #DO NOT MAKE A NEW SURFACE, DRAW TO THE INPUT SURFACE
    x, y = coordinates
    new_coordinates = (x, y + cfg.text_offset)
    text_rectangle = surface.get_rect(topleft=(new_coordinates))
    surface.blit(surface, text_rectangle)

def draw_rectangle(surface, coordinates, rectangle_width, rectangle_height, border=0, color= cfg.BLACK):
    rect_object = (coordinates[0], coordinates[1], rectangle_width, rectangle_width)
    pygame.draw.rect(surface, color, rect_object, border)


def draw_line(surface, start_pos, end_pos, color = cfg.BLACK):
    pygame.draw.line(surface, color, start_pos, end_pos, cfg.line_width)

