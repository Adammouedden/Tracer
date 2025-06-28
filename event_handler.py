import pygame
import pygame.scrap as scrap
import configs as cfg

# Pygame Initialization
pygame.init()

def handle_events(event, running, caps_lock, frame_index, number_of_animation_frames, animation_running, code, cursor_pos, mouse_coords):
    scrap.init()
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
        elif event.key == pygame.K_UP:
            if cursor_pos[0] > 0:
                cursor_pos[0] -= 1  # Move cursor up
                cursor_pos[1] = min(cursor_pos[1], len(code[cursor_pos[0]]))
        elif event.key == pygame.K_DOWN:
            if cursor_pos[0] < len(code) - 1:
                cursor_pos[0] += 1  # Move cursor down
                cursor_pos[1] = min(cursor_pos[1], len(code[cursor_pos[0]]))
        elif event.key == pygame.K_LEFT:
            if cursor_pos[1] > 0:
                cursor_pos[1] -= 1  # Move cursor left
            elif cursor_pos[1] == 0:
                if cursor_pos[0] > 0:
                    cursor_pos[0] -= 1
                    cursor_pos[1] = len(code[cursor_pos[0]])  # Move to the end of the previous line
            frame_index = (frame_index - 1) % number_of_animation_frames
        elif event.key == pygame.K_RIGHT:
            if cursor_pos[1] < len(code[cursor_pos[0]]):
                cursor_pos[1] += 1  # Move cursor right
            elif cursor_pos[1] == len(code[cursor_pos[0]]):
                if cursor_pos[0] < len(code) - 1:
                    cursor_pos[0] += 1
                    cursor_pos[1] = 0  # Move to the start of the next line
            frame_index = (frame_index + 1) % number_of_animation_frames
        elif event.key == pygame.K_RETURN:
            if cursor_pos[1] < len(code[cursor_pos[0]]):
                # Split the current line at the cursor position
                new_line = code[cursor_pos[0]][cursor_pos[1]:] 
                code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]]
                code.insert(cursor_pos[0]+1, new_line)  # Add a new line with the remaining text                
            else:
                code.append("")  # Add a new line to the code array
            cursor_pos[0] += 1  # Move to the next line
            cursor_pos[1] = 0  # Reset character position to the start of the new lin
        elif event.key == pygame.K_BACKSPACE:
            code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]-1] + code[cursor_pos[0]][cursor_pos[1]:]
            if cursor_pos[1] == 0:
                cursor_pos[0] = max(0, cursor_pos[0] - 1)  # Move to the previous line if at the start of the current line
                cursor_pos[1] = len(code[cursor_pos[0]])  # Move to the end of the previous line
            else:
                cursor_pos[1] = max(0, cursor_pos[1] - 1)
        elif event.key == pygame.K_CAPSLOCK:
            caps_lock = not caps_lock
        elif event.key == pygame.K_TAB:
            print("Tab key pressed")
        
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

                    pasted_text = clipboard_data.decode('utf-8')
                    pasted_text = pasted_text.replace('\x00', '')  # Remove null characters
                    pasted_text_length = len(pasted_text)

                # Insert the pasted text at the cursor position
                code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]] + pasted_text + code[cursor_pos[0]][cursor_pos[1]:]
                    
                # Update cursor position and cursor coordinates
                cursor_pos[1] += pasted_text_length  # Move cursor position forward

        # Account for all other keys
        else: 
            if caps_lock:
                event.unicode = event.unicode.upper()
            else:
                event.unicode = event.unicode.lower()
            # Left side of cursor character position + new character + right side of cursor character position
            code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]] + event.unicode + code[cursor_pos[0]][cursor_pos[1]:]
            cursor_pos[1] += 1

    return running, caps_lock, frame_index, animation_running, code, cursor_pos, mouse_coords