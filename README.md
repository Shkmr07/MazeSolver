# Terminal-Based Maze Solver

## Project Description
This project is a terminal-based maze solver implemented in Python. The maze is randomly generated with the help of Python's `random` module. The maze consists of open spaces and walls, with walls occupying approximately 25% of the total area.

## Maze Generation
The maze is generated randomly. Each cell in the maze can either be an open space or a wall. The `random` module is used to decide the type of each cell. After the maze is generated, walls are added to approximately 25% of the cells to create a more complex maze.

## Maze Solver
The maze solver uses the Depth-First Search (DFS) algorithm to find a path through the maze. The DFS algorithm starts at a random cell and explores as far as possible along each branch before backtracking.

## Output
The solvable maze is printed to the terminal. The path found by the DFS algorithm is marked for easy visualization.

![MazeSolver](https://github.com/Shkmr07/MazeSolver/assets/113815453/d9baa493-3538-4295-afd3-63b4d5566730)
