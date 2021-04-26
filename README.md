# Blocks: CellularAutomaton

## Overview
Cellular Automaton has been around since the 20th century. However, Stephen Wolfram's book *A New Kind of Science* released in 2002 brought new interest to the subject. 
Originally conceived in the 1940's by mathematician John Von Neumann, cellular automaton represent any system in which a machine is able to create copies of itself according to specific rules.
This idea was then popularized in John Conway's **Game of Life**. Played on a two dimensional board, each cell lives or dies based on the amount of neighbors that are dead or alive.
Upon mass adoption of the personal computer and the advent of the field of Computer Science, Stephen Wolfram proposed the idea that the universe could function according to cellular automaton rules,
in which a "cell" has knowledge only of its immediate neighbors, and out of countless generations, a seemingly complex system can arise.

## Project Description
The program was implemented with Python:
* Numpy for game state
* qimage2ndarray for conversion from model to image
* PyQt5 for GUI

### The Model
The model was implemented in the `onedim.py` Class.

This class contains all information about the game state and methods to evolve the game state.
##### Attributes:
* x: rows that will be stored in the game state
* y: columns that will be stored in the game state
* gen: current generation
* ruleset: the ruleset that is used to evolve the game state
* map: the current game state

### The GUI
The GUI was implemented in the `gui.py` and `components.py` Classes.

#### `gui.py`
Contains a subclass of `QWidget` that creates and adds all components to the UI. Addtionally, contains methods to handle events that occur during execution.

#### `components.py`
Contains all custom widgets used in the UI. 

## Execution
The game can be launched with `blocks.py`
```bash
$ python3 blocks.py
```

## Demo
https://user-images.githubusercontent.com/31539534/115976911-9b7bbd80-a540-11eb-9452-43aeb43e9480.mov

## Requirements
Software | Version
---------|--------
Python | >= 3.6
PyQt5 | >= 5.15
Numpy | >= 1.20
qimage2ndarray | 1.8.3

## Future Developments
* Planned implementation of 2D and potentially 3D cellular automaton
* Neural Network to take a starting positiion and use the rules to reach another desired position
