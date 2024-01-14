import pygame
    
def get_color(previous, current):
    if previous - current == 1:
        return (255, 0, 0)
    elif previous - current == -1:
        return (0, 255, 0)
    elif current == 1:
        return (255, 255, 255)
    else:
        return (0, 0, 0)

def render(screen, array, new_array, pixel_size):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            pygame.draw.rect(screen, get_color(array[i, j], new_array[i, j]), pygame.Rect(i*pixel_size, j*pixel_size, pixel_size, pixel_size))