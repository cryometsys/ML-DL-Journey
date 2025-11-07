# import math

# scores = [3, 5, 2, 9, 12, 5, 23, 23]
# treedepth = math.log(len(scores), 2)
# print(treedepth)

# def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
#     if(curDepth == targetDepth): return scores[nodeIndex]
#     if(maxTurn):
#         return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth), minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
#     else:
#         return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth), minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))
        
# print(minimax(0, 0, True, scores, treedepth))


### Using visualization; not very important

# import math
# import networkx as nx
# import matplotlib.pyplot as plt

# scores = [3, 5, 2, 9, 12, 5, 23, 23]
# n_leaves = len(scores)
# tree_depth = int(math.log2(n_leaves))  # depth from root (0) to leaves (tree_depth)
# print("Tree depth:", tree_depth)

# # Total nodes in full binary tree: 2^(d+1) - 1
# total_nodes = 2 ** (tree_depth + 1) - 1

# # Build graph with correct 0-based heap indexing
# G = nx.DiGraph()

# # Add all nodes with depth info
# for i in range(total_nodes):
#     depth = (i + 1).bit_length() - 1  # or use math.floor(math.log2(i + 1))
#     G.add_node(i, subset=depth)

# # Add edges
# for i in range(total_nodes // 2):  # only internal nodes
#     left = 2 * i + 1
#     right = 2 * i + 2
#     if left < total_nodes:
#         G.add_edge(i, left)
#     if right < total_nodes:
#         G.add_edge(i, right)

# # Assign labels: internal nodes as "N#", leaves as scores
# labels = {}
# for i in range(total_nodes):
#     if i >= total_nodes // 2:  # leaf nodes
#         leaf_index = i - (total_nodes // 2)
#         labels[i] = str(scores[leaf_index])
#     else:
#         labels[i] = f"N{i}"

# # Layout and draw
# pos = nx.multipartite_layout(G, subset_key="subset")
# nx.draw(G, pos, labels=labels, with_labels=True,
#         node_size=800, node_color="lightblue", font_weight="bold", arrows=False)
# plt.title("Minimax Game Tree (Correct 0-based Heap Indexing)")
# plt.show()

# # Now minimax function must use the same leaf indexing
# def minimax(cur_depth, node_index, is_max, scores, target_depth, leaf_offset):
#     if cur_depth == target_depth:
#         return scores[node_index - leaf_offset]
#     left = minimax(cur_depth + 1, node_index * 2 + 1, not is_max, scores, target_depth, leaf_offset)
#     right = minimax(cur_depth + 1, node_index * 2 + 2, not is_max, scores, target_depth, leaf_offset)
#     return max(left, right) if is_max else min(left, right)

# leaf_start = total_nodes // 2
# result = minimax(0, 0, True, scores, tree_depth, leaf_start)
# print("Minimax result:", result)


### MINIMAX implemented in tic-tac-toe


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

def minimax(board, depth, is_maximizing):
    """Minimax algorithm for the AI to pick the best move."""
    winner = check_winner(board)
    if winner == 'O':  # AI wins
        return 1
    elif winner == 'X':  # Player wins
        return -1
    elif is_full(board):  # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    """Determine the best move for the AI."""
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
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