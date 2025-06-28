import pygame
import configs as cfg

button_width = 100 # Reduced width for icon buttons
button_height = 100 # Adjusted height for icon buttons
button_spacing = 120 # Spacing between buttons

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
        if self.rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=10)

        icon_surface = self.font.render(self.icon_char, True, cfg.BLACK)
        icon_rect = icon_surface.get_rect(center=self.rect.center)

        surface.blit(icon_surface, icon_rect)

    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    if self.action:
                        self.action()



# Button functions
def runCode():
    print("run code pressed")

def forwardVis():
    print("fowardVis Pressed")

def backVis():
    print("backVis Pressed")

# Button instances
runButton = Button(
    x=cfg.WIDTH // 2 - button_width // 2,
    y=cfg.HEIGHT // 2 - button_height // 2 - button_spacing,
    width=button_width, height=button_height,
    icon_char="▶", # Play icon
    color=cfg.GREEN, hover_color=cfg.HIGHLIGHT_YELLOW,
    action=runCode
)


forwardButton = Button(
    x=cfg.WIDTH // 2 - button_width // 2,
    y=cfg.HEIGHT // 2 - button_height // 2 - button_spacing,
    width=button_width, height=button_height,
    icon_char="▶", # Play icon
    color=cfg.GREEN, hover_color=cfg.HIGHLIGHT_YELLOW,
    action=forwardVis
)

backButton = Button(
    x=cfg.WIDTH // 2 - button_width // 2,
    y=cfg.HEIGHT // 2 - button_height // 2 - button_spacing,
    width=button_width, height=button_height,
    icon_char="▶", # Play icon
    color=cfg.GREEN, hover_color=cfg.HIGHLIGHT_YELLOW,
    action=backVis
)


all_buttons = [runButton, forwardButton, backButton]
