import pygame
import configs as cfg
import shapes
# Offset for text rendering
from buttons import text_editor_buttons

OFFSET = 20  # Offset for text rendering
font_size = 24
text_offset = 5
line_height = font_size + text_offset # The total height of one line


def surface(code, cursor_pos, scroll_y_offset):
    text_editor_surface = pygame.Surface((cfg.TEXT_EDITOR_WIDTH, cfg.HEIGHT))
    text_editor_surface.fill(cfg.VS_GREY)
    
    font = pygame.font.SysFont("ubuntu", font_size)
    #font = pygame.font.Font("C:/Windows/Fonts/consola.ttf", font_size) 

    # --- RENDER VISIBLE LINES OF CODE ---
    for i, line in enumerate(code):
        # Calculate the Y position of the line based on the scroll offset
        line_y_pos = OFFSET + ((i - scroll_y_offset) * line_height)

        # Only draw the line if it's within the visible area of the surface
        if line_y_pos > -line_height and line_y_pos < cfg.HEIGHT:
            shapes.draw_text(text_editor_surface, line, (OFFSET, line_y_pos), font_size, cfg.GREEN)

    # --- DRAW THE CURSOR ---
    if (pygame.time.get_ticks() % 1000 < 500):
        # The cursor's Y position must also be adjusted by the scroll offset
        cursor_y_pos = OFFSET + 5 + ((cursor_pos[0] - scroll_y_offset) * line_height)
        
        # Only draw the cursor if its line is visible
        if cursor_pos[0] >= scroll_y_offset and cursor_pos[0] < scroll_y_offset + (cfg.HEIGHT / line_height):
            cursor_rect = pygame.Rect(
                OFFSET + font.size(code[cursor_pos[0]][:cursor_pos[1]])[0], 
                cursor_y_pos, 
                2, 
                font_size
            )
            pygame.draw.rect(text_editor_surface, cfg.GREEN, cursor_rect)


    # --- DRAW THE SCROLLBAR ---
    scrollbar_track_height = cfg.HEIGHT - 2 # The inner height of the scrollbar area

    # Outer line of scrollbar
    pygame.draw.rect(text_editor_surface, cfg.BLACK, (cfg.TEXT_EDITOR_WIDTH - 20, 0, 20, cfg.HEIGHT))
    
    # Inner fill of scrollbar
    pygame.draw.rect(text_editor_surface, cfg.VS_GREY, (cfg.TEXT_EDITOR_WIDTH - 19, 1, 18, scrollbar_track_height))

    # --- SCROLLBAR THUMB LOGIC ---
    total_lines = len(code)
    visible_lines = cfg.HEIGHT / line_height
    
    # The thumb should only be visible if not all lines are visible
    if visible_lines < total_lines:
        # Calculate thumb height: proportional to the ratio of visible content
        thumb_height = max(20, (visible_lines / total_lines) * scrollbar_track_height) # Min height of 20px

        # Calculate thumb position: proportional to how far we've scrolled
        scroll_percentage = scroll_y_offset / (total_lines - visible_lines)
        thumb_y = (scrollbar_track_height - thumb_height) * scroll_percentage

        thumb_rect = pygame.Rect(cfg.TEXT_EDITOR_WIDTH - 19, 1 + thumb_y, 18, thumb_height)
        pygame.draw.rect(text_editor_surface, cfg.VS_LIGHT_GREY, thumb_rect)
        
    return text_editor_surface

def draw_text_editor_buttons(surface):
    for buttons in text_editor_buttons:
        buttons.draw(surface)