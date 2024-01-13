import pygame
import numpy as np
import argparse

from utils.render import render
from utils.theory import rule_value, calc_state

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('--width', type=int, default=999, help='width of the screen')
argument_parser.add_argument('--height', type=int, default=999, help='height of the screen')
argument_parser.add_argument('--rule', type=int, default=22, help='rule of the automata')
argument_parser.add_argument('--frame_rate', type=int, default=30, help='frame rate of the simulation')
argument_parser.add_argument('--pixel_size', type=int, default=5, help='pixel size of the array block')

args = argument_parser.parse_args()

def initialize(rule):
    width = args.width
    height = args.height
    pixel_size = args.pixel_size

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Automata")

    rule = rule_value(rule)
    init_array = np.zeros(shape = int(width/pixel_size), dtype=np.int16)
    init_array[int(width/pixel_size/2)+1] = 1

    return init_array, rule, pixel_size, screen

def automata():
    rule = args.rule
    h = 0
    init_array, rule, pixel_size, screen = initialize(rule)
    array = init_array.copy()
    
    clock = pygame.time.Clock()
    screen.fill((0, 0, 0))
    running = True
    while running:
        new_array = calc_state(array, rule)
        render(new_array, pixel_size, screen, h)

        h += pixel_size
        if h >= args.height:
            h = 0
            pygame.display.update()
        clock.tick(args.frame_rate)
        array = new_array

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

if __name__ == "__main__":
    automata()
