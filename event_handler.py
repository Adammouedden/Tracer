import pygame
import pygame.scrap as scrap
import configs as cfg
from buttons import all_buttons
# Pygame Initialization
pygame.init()

def handle_events(event, running, caps_lock, frame_index, number_of_animation_frames, animation_running, code, cursor_pos, mouse_coords, scroll_y_offset):
    # --- CALCULATE SCROLL LIMITS ---
    # We need to know the max scroll value to avoid scrolling past the end of the code.
    # This calculation should ideally be done once, but for simplicity, we do it here.
    font_size = 24
    text_offset = 5
    line_height = font_size + text_offset
    visible_lines = int(cfg.HEIGHT / line_height)
    max_scroll = max(0, len(code) - visible_lines)


    if event.type == pygame.QUIT:
        running = False 

    elif event.type == pygame.MOUSEMOTION:
        mouse_coords = pygame.mouse.get_pos()

    elif event.type == pygame.MOUSEBUTTONDOWN:
        # --- SCROLL WHEEL LOGIC ---
        if event.button == 4:  # Scroll up
            scroll_y_offset = max(0, scroll_y_offset - 1) # Decrease offset, but not below 0
            print(f"Scrolled up. Offset: {scroll_y_offset}")
        elif event.button == 5:  # Scroll down
            scroll_y_offset = min(max_scroll, scroll_y_offset + 1) # Increase offset, but not past max
            print(f"Scrolled down. Offset: {scroll_y_offset}")

         # --- (Other mouse button logic) ---
        if event.button == 1:  # Left mouse button
            print("Left mouse button clicked at", mouse_coords)
        elif event.button == 3:  # Right mouse button
            print("Right mouse button clicked at", mouse_coords)
        elif event.button == 4:  # Scroll up
            print("Mouse wheel scrolled up at", mouse_coords)
        elif event.button == 5:  # Scroll down
            print("Mouse wheel scrolled down at", mouse_coords)
            
        for buttons in all_buttons:
            print(f"(OG) Frame: {frame_index}/{number_of_animation_frames}")

            frame_index = buttons.handleEvent(event, frame_index, number_of_animation_frames)  # Pass frame_index

    elif event.type == pygame.KEYDOWN:
        # --- SCROLL KEYBOARD LOGIC ---
        if event.mod & pygame.KMOD_CTRL: # Check if Control key is held down
            if event.key == pygame.K_UP:
                scroll_y_offset = max(0, scroll_y_offset - 1)
                print(f"CTRL+UP. Offset: {scroll_y_offset}")
                # We add a return here to prevent the regular K_UP from also firing
                return running, caps_lock, frame_index, animation_running, code, cursor_pos, mouse_coords, scroll_y_offset
            
            if event.key == pygame.K_DOWN:
                scroll_y_offset = min(max_scroll, scroll_y_offset + 1)
                print(f"CTRL+DOWN. Offset: {scroll_y_offset}")
                # We add a return here to prevent the regular K_DOWN from also firing
                return running, caps_lock, frame_index, animation_running, code, cursor_pos, mouse_coords, scroll_y_offset
            
        # --- (Rest of your KEYDOWN logic) ---
        '''
        if event.key == pygame.K_PAGEUP:
            frame_index = (frame_index + 1) % number_of_animation_frames
            print(f"Frame: {frame_index}/{number_of_animation_frames}")
        if event.key == pygame.K_PAGEDOWN:
            frame_index = (frame_index - 1) % number_of_animation_frames
            print(f"Frame: {frame_index}/{number_of_animation_frames}")
        '''
        if event.key == pygame.K_ESCAPE:
            running = False
        elif event.key == pygame.K_UP:
            if cursor_pos[0] > 0:
                # When moving the cursor, make sure the view scrolls if needed!
                if cursor_pos[0] - 1 < scroll_y_offset:
                    scroll_y_offset = cursor_pos[0] - 1
                cursor_pos[0] -= 1  # Move cursor up
                cursor_pos[1] = min(cursor_pos[1], len(code[cursor_pos[0]]))
        elif event.key == pygame.K_DOWN:
            if cursor_pos[0] < len(code) - 1:
                # When moving the cursor, make sure the view scrolls if needed!
                if cursor_pos[0] + 1 >= scroll_y_offset + visible_lines:
                     scroll_y_offset = cursor_pos[0] - visible_lines + 2
                cursor_pos[0] += 1  # Move cursor down
                cursor_pos[1] = min(cursor_pos[1], len(code[cursor_pos[0]]))
        elif event.key == pygame.K_LEFT:
            if cursor_pos[1] > 0:
                cursor_pos[1] -= 1  # Move cursor left
            elif cursor_pos[1] == 0:
                if cursor_pos[0] > 0:
                    cursor_pos[0] -= 1
                    cursor_pos[1] = len(code[cursor_pos[0]])  # Move to the end of the previous line
        elif event.key == pygame.K_RIGHT:
            if cursor_pos[1] < len(code[cursor_pos[0]]):
                cursor_pos[1] += 1  # Move cursor right
            elif cursor_pos[1] == len(code[cursor_pos[0]]):
                if cursor_pos[0] < len(code) - 1:
                    cursor_pos[0] += 1
                    cursor_pos[1] = 0  # Move to the start of the next line
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
            # If the cursor is at the start of the line, move to the previous line
            if cursor_pos[1] == 0:
                # If there is a previous line, merge the current line with the previous one
                if cursor_pos[0] > 0:
                    length_of_previous_line = len(code[cursor_pos[0]-1])
                    # (Previous lines - 1) + previous line + current line + remaining lines
                    code = code[:cursor_pos[0]-1] + [code[cursor_pos[0]-1] + code[cursor_pos[0]]] + code[cursor_pos[0]+1:]
                    #RESET CURSOR POSITION
                    cursor_pos[0] = cursor_pos[0] - 1
                    cursor_pos[1] = length_of_previous_line  # Move to the end of the previous line""

            # If the cursor is not at the start of the line, just move the cursor back
            else:
                code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]-1] + code[cursor_pos[0]][cursor_pos[1]:]
                #RESET CURSOR POSITION
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
                if clipboard_data:
                        try:
                            for t in pygame.scrap.get_types():
                                print(f"DEBUG: Clipboard type: {t}\n")

                                pasted_text = clipboard_data.decode('utf-8')
                                pasted_text = pasted_text.replace('\x0d', '')  # Remove carriage return
                                pasted_text = pasted_text.replace('\x00', '')  # Remove null characters
                                pasted_text_length = len(pasted_text)

                            # Insert the pasted text at the cursor position
                            code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]] + pasted_text + code[cursor_pos[0]][cursor_pos[1]:]
                                
                            # Update cursor position and cursor coordinates
                            cursor_pos[1] += pasted_text_length  # Move cursor position forward
                        except UnicodeDecodeError:
                            print("Could not decode clipboard data as UTF-8.")
                        except Exception as e:
                            print(f"An unexpected error occurred during paste: {e}")

        # Account for all other keys
        else: 
            if caps_lock:
                event.unicode = event.unicode.upper()
            else:
                event.unicode = event.unicode.lower()
            # Left side of cursor character position + new character + right side of cursor character position
            code[cursor_pos[0]] = code[cursor_pos[0]][:cursor_pos[1]] + event.unicode + code[cursor_pos[0]][cursor_pos[1]:]
            cursor_pos[1] += 1

    return running, caps_lock, frame_index, animation_running, code, cursor_pos, mouse_coords, scroll_y_offset
