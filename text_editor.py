import pygame
import pygame.scrap as scrap
pygame.init()
screen = pygame.display.set_mode((800, 600))

scrap.init()
scrap.set_mode(pygame.SCRAP_CLIPBOARD)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Fill the screen with a color (e.g., black)
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()
