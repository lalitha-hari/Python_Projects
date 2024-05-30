def initialize_grid(r, c):
    board = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        board.append(row)
    return board

def display_grid(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="  ")
        print()
    print()

def get_user_input(board, r, c):
    while True:
        col = int(input("Choose the column to drop disc: "))
        if col < 0 or col >= c:
            print("Invalid column. Try again.")
            continue

        count = 0
        for i in range(r):
            if board[i][col] != 0:
                count += 1
        
        if count == r:
            print("Column is full. Try again.")
            continue
        
        return col


def drop_disc(board, r, col, player):
    for i in range(r - 1, -1, -1):
        if board[i][col] == 0:
            board[i][col] = player
            break
    return board

def check_win(board, r, player):
    for i in range(len(board)):
        for j in range(len(board[0]) - 3):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
    
    for i in range(len(board[0])):
        for j in range(r - 3):
            if board[j][i] == player and board[j+1][i] == player and board[j+2][i] == player and board[j+3][i] == player:
                return True
    

    for i in range(r - 3):
        for j in range(len(board[0]) - 3):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    
    for i in range(3, r):
        for j in range(len(board[0]) - 3):
            if board[i][j] == player and board[i-1][j+1] == player and board[i-2][j+2] == player and board[i-3][j+3] == player:
                return True

    return False

def check_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

def switch_player(player):
    if player == 1:
        return 2
    else :
        return 1

def play_game():
    r = 6
    c = 7
    board = initialize_grid(r, c)
    display_grid(board)
    player = 1

    while True:
        col = get_user_input(board, r, c)
        board = drop_disc(board, r, col, player)
        display_grid(board)

        if check_win(board, r, player):
            print(f"Player {player} won the match!")
            break
        elif check_draw(board):
            print("The game is a draw!")
            break

        player = switch_player(player)

play_game()
