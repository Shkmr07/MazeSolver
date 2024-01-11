import random
from termcolor import colored

def MazeSolver(i,j,n,array,visited=[]):
    # This conditions checking the position is vaild or not
    if i < 0 or j < 0 or j == n or i == n or  array[i][j] == colored("▓", "red") or [i,j] in visited:
        return False
    # This conditions is for sucessfully reach at exit point
    if i == n-1 and j == n-1: return True
    
    # Rest all conditions is for checking all four directions
    visited.append([i,j])
    array[i][j] = colored("◍", "green")

    ans = (MazeSolver(i,j+1,n,array,visited) or MazeSolver(i+1,j,n,array,visited) or MazeSolver(i,j-1,n,array,visited) or MazeSolver(i-1,j,n,array,visited))
    visited.pop()

    if ans == False: array[i][j] = colored("◌", "blue")
    
    return ans


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

def print_array(array):
    # Here, creating a grid in such a way the output looks nice with the help of string concatenation.
    for i in range(len(array)):
        st = ""
        for j in range(len(array)):
            st+= "+---"
        print(colored(st+"+","red"))
        print("| ",end="")

        for j in range(len(array)):
            print(array[i][j],end=" | ")
        print()

    st = ""
    for j in range(len(array)):
        st+="+---"
    print(colored(st+"+","red"))

def main():
    # Ask the user for the size of the array (n x n) along with printing random generated maze.
        
    n = int(input("Enter the size of the Maze (n x n): "))
    print("Generated Maze:")
    array = generate_array(n)
    print_array(array)

    # Giving options for user whatever it wants  
    print("1. Print the Path")
    print("2. Generate another puzzle")
    print("3. Exit the Game")
    user_inp = int(input("Enter your choice (1/2/3): "))

   # This loop is running from that time user wants to play the game.
    # when the user select 3 as a choice (means exit the game) then that time loop terminate.
    while user_inp != 3:
        if user_inp == 1:
            print("Maze with Path:")
            MazeSolver(0,1,n,array)
            print_array(array)

        elif user_inp == 2:
            n = int(input("Enter the size of the Maze (n x n): "))
            array = generate_array(n)
            print_array(array)

        print("1. Print the Path")
        print("2. Generate another puzzle")
        print("3. Exit the Game")
        user_inp = int(input("Enter your choice (1/2/3): "))

main()