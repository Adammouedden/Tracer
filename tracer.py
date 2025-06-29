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
import gameState


# Pygame Initialization
pygame.init()

# Screen Variables
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, WINDOW_OFFSET'
screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT - cfg.WINDOW_OFFSET), pygame.RESIZABLE)
pygame.display.set_caption("Tracer")
clock = pygame.time.Clock()

# Initialize Game Variables
state = gameState.GameState()
state.code = [""] # Initial code
animation_frames = build_animation_frames()
number_of_animation_frames = len(animation_frames)

while state.running:
    # Event handling
    for event in pygame.event.get():
        handle_events(event, state, number_of_animation_frames) # Just pass the state object

    # ... drawing logic uses state.code, state.cursor_pos, etc.
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

    # --- Drawing Screen ---
    screen.fill(cfg.WHITE)

    # 1. Clear your sub-surfaces at the beginning of the drawing phase
    visualization_window.fill(cfg.GREEN) # Or whatever its base color is
    text_window.fill(cfg.VS_BLACK)       # Or whatever its base color is

    # 2. Remake and draw the text editor
    text_editor_surface = text_editor.surface(code, cursor_pos)
    screen.blit(text_editor_surface, (0, 0))

    # 3. Draw the animation content onto the CLEAN surfaces
    current_frame = animation_frames[frame_index]
    parse_function_calls(visualization_window, text_window, current_frame) # This should ONLY draw, not fill

    # 4. Blit the results to the screen
    screen.blit(visualization_window, cfg.VIZ_WINDOW_STARTING_COORDINATES)
    screen.blit(text_window, (cfg.VIZ_WINDOW_STARTING_X, cfg.VIZ_WINDOW_HEIGHT + cfg.VIZ_WINDOW_STARTING_Y)) # Blit to the main screen, not the viz_window

    # --- Flipping the display ---
    pygame.display.update()

    # Cap the frame rate
    clock.tick(cfg.FPS)

# Quit Pygame
pygame.quit()
sys.exit()
