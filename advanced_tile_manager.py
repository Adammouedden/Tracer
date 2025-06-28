import pygame
import shapes
import os
import viz_window
import configs as cfg

pygame.init()

# Screen Variables
os.environ['SDL_VIDEO_WINDOW_POS'] = '0, WINDOW_OFFSET'
screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT - cfg.WINDOW_OFFSET))
pygame.display.set_caption("Tracer")

visualization_window = viz_window.create_viz_window(cfg.RED)

WINDOW_HEIGHT = cfg.HEIGHT - cfg.WINDOW_OFFSET
WINDOW_WIDTH = cfg.WIDTH

def create_tile(tile_coordinates):
    new_tile = pygame.Surface(tile_coordinates)
    new_tile.fill(cfg.BLUE)
    return new_tile

colors_array = [cfg.BLUE, cfg.GREEN, cfg.REDz]

def rotating_colors(index):
    color = colors_array[index % 3]
    return color


def draw_to_tile(tile: pygame.Surface, text, index):
    new_color = rotating_colors(index)
    tile.fill(new_color)
    shapes.draw_text(tile, f"{text}", (0,0), font_size=30)


def tiling_manager(tile_height):
    number_of_tiles = WINDOW_HEIGHT // tile_height
    print(number_of_tiles)

    tiles_array = []

    for i in range(number_of_tiles):
        y_coordinate = i * tile_height
        tile_surface = create_tile((WINDOW_WIDTH, tile_height))
        tiles_array.append((tile_surface, (0, y_coordinate)))

    return tiles_array


running = True

tiles_array = tiling_manager(tile_height=50)

for i, (tile_surface, pos) in enumerate(tiles_array):
    draw_to_tile(tile_surface, f"Tile {i+1}", i)

while running:
    screen.blit(visualization_window, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(cfg.BLACK)

    for tile_surface, pos in tiles_array:
        screen.blit(tile_surface, pos)

    pygame.display.update()

pygame.quit()