import pygame
import configs as cfg
import shapes
# Offset for text rendering
from buttons import text_editor_buttons

OFFSET = 20  # Offset for text rendering
font_size = 24
text_offset = 5

def surface(code, cursor_pos):
    text_editor_surface = pygame.Surface((cfg.TEXT_EDITOR_WIDTH, cfg.HEIGHT))
    text_editor_surface.fill(cfg.BLACK)
    
    font = pygame.font.SysFont("ubuntu", font_size)

    # Render each line of code
    for i, line in enumerate(code):
        shapes.draw_text(text_editor_surface, line, (OFFSET, OFFSET + (i*(font_size+text_offset))), font_size, cfg.GREEN)

    # Drawing the cursor
    if (pygame.time.get_ticks() % 1000 < 500):
        cursor_rect = pygame.Rect(OFFSET+font.size(code[cursor_pos[0]][:cursor_pos[1]])[0], OFFSET + 5 + (cursor_pos[0]*(font_size+text_offset)), 2, font_size)
        pygame.draw.rect(text_editor_surface, cfg.GREEN, cursor_rect)

    return text_editor_surface

def draw_text_editor_buttons(surface):
    for buttons in text_editor_buttons:
        buttons.draw(surface)

