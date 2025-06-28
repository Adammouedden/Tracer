import pygame
import configs as cfg
import shapes

def surface(code, cursor_pos, cursor_coords, ):
    text_editor_surface = pygame.Surface((cfg.TEXT_EDITOR_WIDTH, cfg.HEIGHT))
    text_editor_surface.fill(cfg.BLACK)
    font_size = 24
    font = pygame.font.SysFont("ubuntu", font_size)

    # Render each line of code
    for i, line in enumerate(code):
        shapes.draw_text(text_editor_surface, line, (30,30))

    # Drawing the cursor
    if (pygame.time.get_ticks() % 1000 < 500):
        cursor_rect = pygame.Rect(cursor_coords[0], cursor_coords[1], 2, font_size)
        pygame.draw.rect(text_editor_surface, cfg.GREEN, cursor_rect)

    return text_editor_surface