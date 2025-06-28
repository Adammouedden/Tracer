import pygame
import configs as cfg
import shapes

OFFSET = 30  # Offset for text rendering

def surface(code, cursor_pos):
    text_editor_surface = pygame.Surface((cfg.TEXT_EDITOR_WIDTH, cfg.HEIGHT))
    text_editor_surface.fill(cfg.BLACK)
    font_size = 50
    font = pygame.font.SysFont("ubuntu", font_size)

    # Render each line of code
    for i, line in enumerate(code):
        print(line)
        shapes.draw_text(text_editor_surface, line, (OFFSET, OFFSET + (i*font_size)), font_size, cfg.GREEN)

    # Drawing the cursor
    if (pygame.time.get_ticks() % 1000 < 500):
        cursor_rect = pygame.Rect(OFFSET+font.size(code[cursor_pos[0]][:cursor_pos[1]])[0], OFFSET + (cursor_pos[0]*font_size), 2, font_size)
        pygame.draw.rect(text_editor_surface, cfg.GREEN, cursor_rect)

    return text_editor_surface