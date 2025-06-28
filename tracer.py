# Module imports
import os
import pygame
import sys

# File imports
import configs as cfg
import header
import text_editor
import viz_window

# Game Loop Logic
#------------------------------------------------------------------------------------------------------------------------
# Running Variables
running = True
animation_running = False

# Position Variables
mouse_coords = [0, 0]
text_pos = [0, 0]
text_coords = [0, 0]

# Initialize Game Variables
code = [""]
current_frame_index = 0

# Initialize Surfaces


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
                pass
            elif event.button == 3:  # Right mouse button
                pass
            elif event.button == 4:  # Scroll up
                pass
            elif event.button == 5:  # Scroll down
                pass
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                animation_running = not animation_running

    # Drawing Screen   
    cfg.screen.fill(cfg.WHITE)
    
    # Flipping the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()