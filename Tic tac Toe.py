import math

# Initialize board
board = [" "] * 9

# Function to print board
def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check winner
def check_win(player):
    win_pos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for pos in win_pos:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(is_max):
    if check_win("O"): return 1
    if check_win("X"): return -1
    if is_draw(): return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

# Find best move for computer
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game
print("Tic Tac Toe: You are X, Computer is O")
print_board()

while True:
    # Human move
    move = int(input("Enter your move (1-9): ")) - 1
    if board[move] != " ":
        print("Already taken! Try again.")
        continue
    board[move] = "X"
    print_board()
    if check_win("X"):
        print("🎉 You win!")
        break
    if is_draw():
        print("It's a draw!")
        break

    # Computer move
    print("Computer is thinking...")
    board[best_move()] = "O"
    print_board()
    if check_win("O"):
        print("💻 Computer wins!")
        break
    if is_draw():
        print("It's a draw!")
        break
