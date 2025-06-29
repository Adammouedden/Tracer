import pygame
from Agentic_AI.tracer_compiler import build_animation_frames
import configs as cfg

class Button:
    def __init__(self, x, y, width, height, icon_char,color, hover_color, action=None, icon_font_size=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.icon_char = icon_char
        self.color = color
        self.current_color = color
        self.hover_color = color
        self.action = action

        # Dynamically change the size
        if icon_font_size is None:
            self.font = pygame.font.Font(None, int(height * 0.7)) # Icon takes about 70% of button height
        else:
            self.font = pygame.font.Font(None, icon_font_size)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = (mouse_pos[0]-cfg.TEXT_EDITOR_WIDTH, mouse_pos[1])
        #print(f"mouse pos: {mouse_pos} self rect: {self.rect} collide: {self.rect.collidepoint(mouse_pos)}")
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=10)

        icon_surface = self.font.render(self.icon_char, True, cfg.BLACK)
        icon_rect = icon_surface.get_rect(center=self.rect.center)

        surface.blit(icon_surface, icon_rect)

    def handleEvent(self, event, frame_index, number_of_animation_frames, code):
        mouse_pos = pygame.mouse.get_pos()
        if self.action == "viz_forward" or self.action == "viz_backward":
            mouse_pos = (mouse_pos[0]-cfg.TEXT_EDITOR_WIDTH, mouse_pos[1])
        print(f"mouse pos: {mouse_pos} self rect: {self.rect} collide: {self.rect.collidepoint(mouse_pos)}")
        if self.rect.collidepoint(mouse_pos):
            print(f"Button {self.icon_char} clicked at {mouse_pos}")
            if self.action == "viz_forward" or self.action == "viz_backward":
                print(f"Frame: {frame_index}/{number_of_animation_frames}")

                frame_index = self.action(frame_index, number_of_animation_frames, code)  # Pass dummy values for now
                return frame_index
            else:
                #Turn code into 1D
                single_string = "\n".join(code)
                animation_frames = self.action(single_string)
                print(f"Animation frames built: {len(animation_frames)}")
            return animation_frames

# Button functions
def runCode(code):
    animation_frames = build_animation_frames(code)
    return animation_frames

def viz_forward(frame_index, number_of_animation_frames):
    #print(f"Frame: {frame_index}/{number_of_animation_frames}")
    frame_index = (frame_index + 1) % number_of_animation_frames
    
    return frame_index

def viz_backward(frame_index, number_of_animation_frames):
    #print(f"Frame: {frame_index}/{number_of_animation_frames}")
    frame_index = (frame_index - 1) % number_of_animation_frames
    return frame_index

VERTICAL_OFFSET_FROM_BOTTOM = 10

# Button instances
runButton = Button(
    x = cfg.TEXT_EDITOR_WIDTH - cfg.button_width -  cfg.button_margin,# Right edge of text editor area - button width - margin
    y = cfg.HEIGHT - cfg.WINDOW_OFFSET - cfg.button_height - cfg.button_margin, # Bottom of screen - offset - button height - margin
    width = cfg.button_width,
    height = cfg.button_height,
    icon_char = "R", # Play icon
    color = cfg.WHITE,
    hover_color = cfg.HIGHLIGHT_YELLOW,
    action = runCode
)

forwardButton = Button(
    x = cfg.VIZ_WINDOW_WIDTH - cfg.button_width - cfg.button_margin, # Right edge of viz window - button width - margin
    y = cfg.VIZ_WINDOW_HEIGHT - cfg.button_height - cfg.button_margin - VERTICAL_OFFSET_FROM_BOTTOM, # Bottom of viz window - button height - margin - offset
    width = cfg.button_width,
    height = cfg.button_height,
    icon_char = "F", # Forward icon
    color = cfg.WHITE,
    hover_color = cfg.HIGHLIGHT_YELLOW,
    action = viz_forward
)

backButton = Button(
    x = forwardButton.rect.x - cfg.button_width - cfg.button_spacing, # Left of forward button - its width - spacing
    y = forwardButton.rect.y, # Same vertical position as forward button
    width = cfg.button_width,
    height = cfg.button_height,
    icon_char = "B", # Backward icon
    color = cfg.WHITE,
    hover_color = cfg.HIGHLIGHT_YELLOW,
    action = viz_backward
)

text_editor_buttons = [runButton]
viz_window_buttons = [forwardButton, backButton]
all_buttons = [runButton, forwardButton, backButton]
