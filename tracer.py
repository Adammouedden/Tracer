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
cursor_pos = [0, 0]   # Line number, character position
cursor_coords = [0, 30]  # X, Y coordinates for text rendering

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
            elif event.key == pygame.K_RIGHT:
                print("Right arrow key pressed")
            elif event.key == pygame.K_RETURN:
                print("Enter key pressed")
            elif event.key == pygame.K_BACKSPACE:
                print("Backspace key pressed")
            elif event.key == pygame.K_CAPSLOCK:
                print("Caps Lock key pressed")
            elif event.key == pygame.K_TAB:
                print("Tab key pressed")
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                print("Shift key pressed")
            
            # --- Copy/Paste/Cut Logic ---  
            elif (event.mod & pygame.KMOD_CTRL): # Check for Control key
                if event.key == pygame.K_c: # Letter C
                    print("CTRL + C pressed")
                    text_to_copy = ""

                    # Collect text to copy from code array
                    for line in code:
                        for character in line:
                            text_to_copy += character
                    
                    # Copy text to clipboard
                    pygame.scrap.put(pygame.SCRAP_TEXT, text_to_copy.encode('utf-8'))
                    print("Text copied to clipboard:", text_to_copy)
                elif event.key == pygame.K_v: # Letter V
                    clipboard_data = pygame.scrap.get(pygame.SCRAP_TEXT)
                    for t in pygame.scrap.get_types():
                        print(f"DEBUG: Clipboard type: {t}\n")
                    try:
                        pasted_text = clipboard_data.decode('utf-8')
                        pasted_text = pasted_text.replace('\x00', '')  # Remove null characters
                        pasted_text_length = len(pasted_text)

                        # Loop over text to insert into code array
                        for i in range(pasted_text_length):
                            code[cursor_pos[0]][cursor_pos[1+i]] = pasted_text[i] # Only deal with the first line for simplicity
                            
                            # Update cursor position and cursor coordinates
                            cursor_pos[1] += 1  # Move cursor position forward
                            cursor_coords[1] += pygame.font.Font.size(cfg.font, pasted_text[i])[0]  # Update text coordinates
                    except UnicodeDecodeError:
                            print("Could not decode clipboard data as UTF-8.")
                    except Exception as e:
                        print(f"An unexpected error occurred during paste: {e}")

            # Account for all other keys
            else:   
                # Left side of cursor character position + new character + right side of cursor character position
                code[cursor_pos[1]] = code[cursor_pos[1]][:cursor_pos[0]] + event.unicode + code[cursor_pos[1]][cursor_pos[0]:]
                cursor_coords[0] += len(event.unicode)
                cursor_pos[0] += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Space key released")

    # Drawing Screen   
    cfg.screen.fill(cfg.WHITE)

    # Remaking and drawing surface
    

    # Flipping the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()