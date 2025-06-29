# Module imports
#HUGE CMMENT
import os
import pygame
import sys

# File imports
import configs as cfg
from event_handler import handle_events
from Agentic_AI.tracer_compiler import build_animation_frames, parse_function_calls
import text_editor
import viz_window
from buttons import all_buttons
from Agentic_AI.tracer_compiler import build_animation_frames, parse_function_calls
import basic_tiling_manager
import shapes

# Pygame Initialization
pygame.init()

# Screen Variables
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, WINDOW_OFFSET'
screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT - cfg.WINDOW_OFFSET))
pygame.display.set_caption("Tracer")
clock = pygame.time.Clock()

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
code = [""]
current_frame_index = 0

# Initialize Surfaces
visualization_window = viz_window.create_viz_window(cfg.GREEN)
text_editor_surface = text_editor.surface(code, cursor_pos)
text_window = basic_tiling_manager.create_text_window()



#BUILD ANIMATION FRAMES
animation_frames = build_animation_frames(code)
print(animation_frames)
number_of_animation_frames = len(animation_frames)
frame_index = 0

# Game Loop
while running:
    # Event handling
    for event in pygame.event.get():  
        running, caps_lock, frame_index, animation_running, code, cursor_pos, mouse_coords \
        = handle_events(event, running, caps_lock, frame_index, number_of_animation_frames, animation_running, code, cursor_pos, mouse_coords)

    # Drawing Screen   
    screen.fill(cfg.WHITE)

    # Remaking and drawing surface
    text_editor_surface = text_editor.surface(code, cursor_pos)
    screen.blit(text_editor_surface, (0,0))

 
    #Draw the animation current frame's functions to the screen
    current_frame = animation_frames[frame_index]
    parse_function_calls(visualization_window, text_window, current_frame)

    #Drawing the visualization window
    screen.blit(visualization_window, (cfg.VIZ_WINDOW_STARTING_COORDINATES))

    #Drawing the text window
    visualization_window.blit(text_window, (0,cfg.VIZ_WINDOW_HEIGHT))
    text_window.fill(cfg.BLUE)

    #Drawing the current frame as text
    shapes.draw_text(text_window, f"{frame_index}/{number_of_animation_frames}", (cfg.WIDTH//4, cfg.TEXT_WINDOW_HEIGHT//2), 30)

    # Flipping the display
    pygame.display.update()
    # Cap the frame rate
    clock.tick(cfg.FPS)

# Quit Pygame
pygame.quit()
sys.exit()
