## Introduction

Conway's Game of Life is a classic cellular automaton devised by mathematician John Conway. It operates on a two-dimensional grid of cells, where each cell can be either alive or dead. The system evolves through discrete generations, with each generation determined by a set of simple rules.

At each step, a living cell survives to the next generation if it has 2 or 3 living neighbors; otherwise, it dies due to underpopulation or overpopulation. A dead cell becomes alive in the next generation if it has exactly 3 living neighbors, illustrating the emergence of new life.

![Screenshot from 2024-02-05 22-55-57](https://github.com/Rebantadey/Cellular-Automata/assets/109721829/5ec023bf-6b4e-470b-ba8a-c4674a8751dd)

What makes the Game of Life intriguing is its capacity for producing complex and diverse patterns from initially simple configurations. Users can create intricate structures, oscillators, gliders, and even self-replicating patterns. The system's sensitivity to initial conditions and the dynamic interplay of neighboring cells lead to the emergence of visually captivating, unpredictable behaviors.

The Game of Life has applications in various fields, such as computer science and artificial life research, serving as a paradigm for studying emergent phenomena and illustrating how simple rules can give rise to complex, self-organizing patterns in a simulated world.

## Usage
1. Install the dependencies
2. run the following command
  ```bash
  python game_of_life.py --width WIDTH --height HEIGHT --frame_rate FRAME_RATE --pixel_size PIXEL_SIZE --probability PROBABILITY
  ```
where
- WIDTH and HEIGHT represent the dimensions of the pygame window.
- FRAME_RATE determines the frame rate of the simulation.
- PIXEL_SIZE represents the block size of each cell in the simulation.
- PROBABILITY denotes the probability of living cell in generation 0.
