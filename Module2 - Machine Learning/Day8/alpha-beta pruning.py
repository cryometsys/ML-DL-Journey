import math

# Initialize the board
board = [' ' for _ in range(9)]

def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()

def check_winner(board):
    """Check if there's a winner on the board."""
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

def is_full(board):
    """Check if the board is full."""
    return ' ' not in board

def alpha_beta(board, depth, alpha, beta, is_maximizing):
    """Alpha-Beta Pruning algorithm for the AI to pick the best move."""
    winner = check_winner(board)
    if winner == 'O':  # AI wins
        return 1
    elif winner == 'X':  # Player wins
        return -1
    elif is_full(board):  # Tie
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def best_move(board):
    """Determine the best move for the AI."""
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    """Main function to play the game."""
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player move
        player_move = int(input("Enter your move (1-9): ")) - 1
        if board[player_move] == ' ':
            board[player_move] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        print_board(board)

        # Check for player win or tie
        if check_winner(board) == 'X':
            print("Congratulations, you win!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

        # AI move
        ai_move = best_move(board)
        board[ai_move] = 'O'
        print("AI has made its move:")
        print_board(board)

        # Check for AI win or tie
        if check_winner(board) == 'O':
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a tie!")
            break

# Run the game
play_game()

