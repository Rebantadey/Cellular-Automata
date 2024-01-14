import numpy as np
import pygame
import argparse

from utils.render import render
from utils.theory import calc_state

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--width', type=int, default=1920, help='width of the screen')
argument_parser.add_argument('--height', type=int, default=1080, help='height of the screen')
argument_parser.add_argument('--frame_rate', type=int, default=100, help='frame rate of the simulation')
argument_parser.add_argument('--pixel_size', type=int, default=7, help='pixel size of the array block')
argument_parser.add_argument('--probability', type=float, default=0.075, help='probability of the cell being alive in initial state')

args = argument_parser.parse_args()

def initialize():
    width = args.width
    height = args.height
    pixel_size = args.pixel_size
    probability = args.probability

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game of Life")

    init_array = np.random.choice([0, 1], size=(int(width/pixel_size), int(height/pixel_size)), p=[1-probability, probability])

    return init_array, pixel_size, screen

def calc(new_array, old_array):
    flag = new_array - old_array
    birth = np.count_nonzero(flag == 1)
    death = np.count_nonzero(flag == -1)

    return birth, death

def automata():
    init_array, pixel_size, screen = initialize()
    array = init_array.copy()

    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    running = True

    birth = np.array([])
    dead = np.array([])

    while running:
        new_array = calc_state(array)
        render(screen, array, new_array, pixel_size)
        
        birth, dead = np.append(birth, calc(new_array, array)[0]), np.append(dead, calc(new_array, array)[1])
        
        pygame.display.update()
        clock.tick(args.frame_rate)
     
        array = new_array

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

if __name__ == "__main__":
    automata()