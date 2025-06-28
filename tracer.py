# Module imports
import os
import pygame
import sys

# File imports
import configs as cfg
<<<<<<< HEAD
=======
import header
>>>>>>> 7ac4e7f7a4c61065da87321ca6864d7bc0992ec7
#import text_editor
import viz_window
from Agentic_AI.tracer_compiler import build_animation_frames, parse_function_calls 

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

# Position Variables
mouse_coords = [0, 0]
text_pos = [0, 0]   # Line number, character position
text_coords = [0, 30]  # X, Y coordinates for text rendering

# Initialize Game Variables
code = [""]

# Initialize Surfaces
visualization_window = viz_window.create_viz_window(cfg.GREEN)

#Build animation frames
animation_frames = build_animation_frames()
frame_index = 0
number_of_animation_frames = len(animation_frames)

print(animation_frames)

# Game Loop
while running:
    # Event handling
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False 

        elif event.type == pygame.MOUSEMOTION:
            mouse_coords = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                print("Left mouse button clicked at", mouse_coords)
            elif event.button == 3:  # Right mouse button
                print("Right mouse button clicked at", mouse_coords)
            elif event.button == 4:  # Scroll up
                print("Mouse wheel scrolled up at", mouse_coords)
            elif event.button == 5:  # Scroll down
                print("Mouse wheel scrolled down at", mouse_coords)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                animation_running = not animation_running
            elif event.key == pygame.K_UP:
                print("Up arrow key pressed")   
            elif event.key == pygame.K_DOWN:
                print("Down arrow key pressed")
            elif event.key == pygame.K_LEFT:
                print("Left arrow key pressed")
                #Go backward in animation frames
                frame_index = (frame_index - 1) % number_of_animation_frames
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
                #Go forward in animation frames
                frame_index = (frame_index + 1) % number_of_animation_frames
            elif event.key == pygame.K_RETURN:
                print("Enter key pressed")
            elif event.key == pygame.K_BACKSPACE:
                code[0] = code[0][:text_pos-1] + code[0][text_pos:]
                text_pos = max(0, text_pos - 1)
            elif event.key == pygame.K_CAPSLOCK:
                print("Caps Lock key pressed")
            elif event.key == pygame.K_TAB:
                print("Tab key pressed")
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                print("Shift key pressed")  
            elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                print("Control key pressed")
            else:   
                # Left side of cursor character position + new character + right side of cursor character position
                code[text_pos[1]] = code[text_pos[1]][:text_pos[0]] + event.unicode + code[text_pos[1]][text_pos[0]:]
                text_coords[0] += len(event.unicode)
                text_pos[0] += 1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Space key released")

    # Drawing Screen   
    screen.fill(cfg.WHITE)

    # Remaking and drawing surface
    current_frame = animation_frames[frame_index]
    parse_function_calls(visualization_window, current_frame)
    

    # Flipping the display
    pygame.display.update()
    # Cap the frame rate
    clock.tick(4)

# Quit Pygame
pygame.quit()
sys.exit()