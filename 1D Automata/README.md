## Introduction

One-dimensional cellular automata (1D CA) are computational models that consist of a linear arrangement of cells, each in one of two possible states (often represented as 0 or 1). The evolution of the system occurs over discrete time steps. At each step, the state of each cell is updated based on a rule that considers its current state and the states of its immediate neighbors. The rule defines the new state of a cell as a function of the current configuration. 1D cellular automata exhibit diverse behaviors, ranging from stable and repetitive patterns to complex and chaotic dynamics, making them a fundamental concept in the study of emergent complexity.

![Screenshot from 2024-02-05 23-03-43](https://github.com/Rebantadey/Cellular-Automata/assets/109721829/94320e87-0bf8-4dde-bd1f-c1d376d44eb9)

## Usage
1. Install the dependencies
2. run the following command
  ```bash
  python 1D_automata.py --width WIDTH --height HEIGHT --frame_rate FRAME_RATE --pixel_size PIXEL_SIZE --probability PROBABILITY
  ```
where
- WIDTH and HEIGHT represent the dimensions of the pygame window.
- FRAME_RATE determines the frame rate of the simulation.
- PIXEL_SIZE represents the block size of each cell in the simulation.
- PROBABILITY denotes the probability of living cell in generation 0.
