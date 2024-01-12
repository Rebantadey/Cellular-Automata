import pygame

def render(array, pixel_size, screen, h):
    for i in range(len(array)):
        pygame.draw.rect(screen, get_color(array[i]), pygame.Rect(i*pixel_size, h, pixel_size, pixel_size))
    pygame.display.flip()

def get_color(value):
    if value == 0:
        return (0, 0, 0)
    else:
        return (67, 78, 42)