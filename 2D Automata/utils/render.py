import pygame

def get_color(value):
    if value == 0:
        return (0, 0, 0)
    else:
        return (11, 219, 230)

def render(screen, array, pixel_size):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            pygame.draw.rect(screen, get_color(array[i, j]), pygame.Rect(i*pixel_size, j*pixel_size, pixel_size, pixel_size))