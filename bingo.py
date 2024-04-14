import random

# Function to generate a random bingo board
def generateBoard():
    board = []
    for i in range(5):
        l = []
        for j in range(5):
            k = random.randint(1, 101)
            l.append(k)
        board.append(l)
    return board

# Function to display the bingo board
def displayBoard(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()

# Function to mark a number on the bingo board
def markNumber(board, number):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == number:
                board[i][j] = 'X'
    return board

# Function to get a number input from the user
def getUserNumber():
    while(True):
        try:
            print("enter input")
            n = int(input())
            if(n >= 1 and n <= 100):
                break
            else:
                print("number should be in between 1 and 100")
        except:
            print("invalid")
    return n

# Function to check if a player has won the bingo game
def checkWin(board):
    # Check rows
    for i in board:
        k = ""
        for j in i:
            k += str(j)
        if k == "XXXXX":
            return True
    
    # Check columns
    for i in range(len(board)):
        k = ""
        for j in range(len(board)):
            k += str(board[j][i])
        if k == "XXXXX":
            return True

    # Check diagonal from top-left to bottom-right
    k = ""
    for i in range(len(board)):
        k += str(board[i][i])
    if k == "XXXXX":
        return True

    # Check diagonal from top-right to bottom-left
    k = ""
    for i in range(len(board)):
        k += str(board[i][len(board)-1-i])
    if k == "XXXXX":
        return True

    return False

# Function to play the bingo game
def playBingoGame():
    print("Welcome to Bingo!")
    board = generateBoard()
    displayBoard(board)
    k = 0 
    while(True):
        if(k > 10):
            break
        n = getUserNumber()
        k += 1
        markNumber(board, n)
        p = checkWin(board)
        if p == True:
            print("Congratulations, you won!")
            break
        else:
            print("Keep trying!")
        displayBoard(board)

# Main function to start the game
playBingoGame()
