import random

def initialize_grid():
    light_board = []
    for i in range(5):
        row = []
        for j in range(5):
            n = random.randint(0, 1)
            row.append(n)
        light_board.append(row)
    return light_board

def print_grid(grid):
    for i in range(5):
        for j in range(5):
            print(grid[i][j], end=' ')
        print(" ")

def get_user_input():
    r = input("Select row from 0 to 4, or 'q' to quit, or 'r' to restart: ")
    if r.lower() == 'q':
        return 'q', 'q'
    if r.lower() == 'r':
        return 'r', 'r'
    c = input("Select column from 0 to 4, or 'q' to quit, or 'r' to restart: ")
    return r, c

def toggle_light(grid, r, c):
    toggles = [(r, c), (r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]
    for i, j in toggles:
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = 0
    return grid

def check_win(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return False
    return True

def game():
    print("Welcome to the game of Lights Out!")
    grid = initialize_grid()
    print_grid(grid)

    while True:
            r, c = get_user_input()
            if r == 'q' or c == 'q':
                print("Thanks for playing! Goodbye.")
                return
            elif r == 'r' or c == 'r':
                print("Restarting the game...")
                break

            r, c = int(r), int(c)
            grid = toggle_light(grid, r, c)
            print_grid(grid)
            if check_win(grid):
                print("Congratulations, you won the game!")
                break

    restart = input("Do you want to play again? (yes/no): ")
    if restart.lower() != 'yes':
        print("Thanks for playing! Goodbye.")
    
    else:
        game()
game()
