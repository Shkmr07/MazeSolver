import random
from termcolor import colored


def generate_array(n):
    # Initialize a 2D array with n rows and n columns
    array = [[colored("◌", "blue") for _ in range(n)] for _ in range(n)]
    
    # Then set (0,0) in "S" and (n-1,n-1) in "E"
    array[0][0] = "S"
    array[n-1][n-1] = "E"

    # Calculate the 25% of total cells to increase the likelihood of a solvable maze.
    max_ones = n * n // 4 

    # Fill the array with red walls in random order
    ones_count = 0
    while ones_count < max_ones:
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)

        # We don't put red walls on the start or end cells
        if (x == 0 and y == 0) or (x == n-1 and y == n-1) or (x == n-2 and y == n-1) or (x == 0 and y == 1):
            continue

        # Place a red wall
        array[x][y] = colored("▓", "red")
        ones_count += 1

    return array
