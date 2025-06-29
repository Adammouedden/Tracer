

class GameState:
    def __init__(self):
        self.running = True
        self.caps_lock = False
        self.mouse_coords = [0, 0]
        self.cursor_pos = [0, 0]  # [line, char_pos]
        self.code = [""]
        self.frame_index = 0
        self.animation_running = False
        # Add other relevant state here