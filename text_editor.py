import pygame
import configs as cfg

def surface(code, cursor_pos, cursor_coords, ):
    text_editor_surface = pygame.Surface((cfg.TEXT_EDITOR_WIDTH, cfg.HEIGHT))
    text_editor_surface.fill(cfg.BLACK)
    font = pygame.font.SysFont("ubuntu", 24)

    # Render each line of code
    for i, line in enumerate(code):
        text_surface = font.render(line, True, cfg.WHITE)
        text_y = cursor_coords[1] + i * (text_surface.get_height() + 5)

    # Drawing the cursor
    
    return text_editor_surface