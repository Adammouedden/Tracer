import pygame
import configs as cfg
from buttons import all_buttons
# Pygame Initialization
pygame.init()

def handle_events(event, running, frame_index, number_of_animation_frames, animation_running, code, cursor_pos, mouse_coords):
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

        for buttons in all_buttons:
            buttons.handleEvent(event)

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
        elif event.key == pygame.K_UP:
            print("Up arrow key pressed")   
        elif event.key == pygame.K_DOWN:
            print("Down arrow key pressed")
        elif event.key == pygame.K_LEFT:
            print("Left arrow key pressed")
            frame_index = (frame_index - 1) % number_of_animation_frames
        elif event.key == pygame.K_RIGHT:
            print("Right arrow key pressed")
            frame_index = (frame_index + 1) % number_of_animation_frames
        elif event.key == pygame.K_RETURN:
            print("Enter key pressed")
        elif event.key == pygame.K_BACKSPACE:
            code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]-1] + code[cursor_pos[0]][cursor_pos[1]:]
            cursor_pos[1] = max(0, cursor_pos[1] - 1)
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
                except UnicodeDecodeError:
                        print("Could not decode clipboard data as UTF-8.")
                except Exception as e:
                    print(f"An unexpected error occurred during paste: {e}")

        # Account for all other keys
        else:   
            # Left side of cursor character position + new character + right side of cursor character position
            code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]] + event.unicode + code[cursor_pos[0]][cursor_pos[1]:]
            cursor_pos[1] += 1

    return running, frame_index, animation_running, code, cursor_pos, mouse_coords
