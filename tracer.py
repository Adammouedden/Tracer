# Module imports
#HUGE CMMENT
import os
import pygame
import sys

# File imports
import configs as cfg
from event_handler import handle_events, event_button_clicked
from Agentic_AI.tracer_compiler import build_animation_frames, parse_function_calls
import text_editor
import viz_window
from buttons import all_buttons
import basic_tiling_manager
import shapes

# Pygame Initialization
pygame.init()

# Screen Variables
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, WINDOW_OFFSET'
screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT - cfg.WINDOW_OFFSET), pygame.RESIZABLE)
pygame.display.set_caption("Tracer")
clock = pygame.time.Clock()
pygame.scrap.init()
# Game Loop Logic
#------------------------------------------------------------------------------------------------------------------------
# Running Variables
running = True
animation_running = False
caps_lock = False

# Position Variables
mouse_coords = [0, 0]
cursor_pos = [0, 0]   # Line number, character position

# Initialize Game Variables
code = [""] #* 50 #TODO: test scrolling with this
current_frame_index = 0
scroll_y_offset = 0

# Initialize Surfaces
visualization_window = viz_window.create_viz_window(cfg.VS_LIGHTBLUE)
text_editor_surface = text_editor.surface(code, cursor_pos, scroll_y_offset)
text_window = basic_tiling_manager.create_text_window()



#BUILD ANIMATION FRAMES
animation_frames = []
number_of_animation_frames = 0
frame_index = 0
current_frame = 0
run_pressed = False

# Game Loop
while running:
    # Event handling
    for event in pygame.event.get():  
        running, caps_lock, code, cursor_pos, mouse_coords, scroll_y_offset \
        = handle_events(event, running, caps_lock, code, cursor_pos, mouse_coords, scroll_y_offset)

        animation_frames, current_frame, run_pressed, frame_index = event_button_clicked(event, animation_frames, code, current_frame, run_pressed, frame_index)
        
    number_of_animation_frames = len(animation_frames) if animation_frames else 0
   
    parse_function_calls(visualization_window, text_window, current_frame)
    if number_of_animation_frames > 0:
        shapes.draw_text(text_window, f"{frame_index}/{number_of_animation_frames}", (700,30), font_size=30, color=cfg.WHITE)
        print(animation_frames)
    #Drawing the visualization window
    screen.blit(visualization_window, (cfg.VIZ_WINDOW_STARTING_COORDINATES))
    
    # Remaking and drawing surface
    text_editor_surface = text_editor.surface(code, cursor_pos, scroll_y_offset)
    text_editor.draw_text_editor_buttons(text_editor_surface)
    viz_window.draw_viz_buttons(visualization_window)
    screen.blit(text_editor_surface, (0,0)) 

    #Drawing the text window
    visualization_window.blit(text_window, (0,cfg.VIZ_WINDOW_HEIGHT))
    text_window.fill(cfg.VS_BLACK)

    # Flipping the display
    pygame.display.update()
    # Cap the frame rate
    clock.tick(cfg.FPS)

# Quit Pygame
pygame.quit()
sys.exit()
