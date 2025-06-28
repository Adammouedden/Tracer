import pygame


pygame.init()


text_offset = 30

#Base Shapes
def draw_text(surface, text: str, coordinates, font_size = 20, color = BLACK):
    font = pygame.font.SysFont("ubuntu", font_size)
    text_surface = font.render(text, True, color)
    x, y = coordinates
    new_coordinates = (x, y + text_offset)
    text_rectangle = text_surface.get_rect(topleft=(new_coordinates))
    surface.blit(text_surface, text_rectangle)

def draw_rectangle(surface, coordinates, rectangle_width, rectangle_height, border=0, color=BLACK):

def draw_line(surface, start_pos, end_pos, color=BLACK):
    pygame.draw.line(surface)
