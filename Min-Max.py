import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.player = 'X'  # 'X' starts by default
        self.computer = 'O'

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i * 3 + j], end=' ')
            print()

    def is_valid_move(self, move):
        return 0 <= move <= 8 and self.board[move] == ' '

    def make_move(self, move, player):
        self.board[move] = player

    def is_winner(self, player):
        win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6))
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def is_board_full(self):
        return all(cell != ' ' for cell in self.board)

    def minimax(self, depth, is_maximizing):
        """
        Recursive MiniMax algorithm to find the best move for the maximizing or minimizing player.

        Args:
            depth (int): The current depth in the search tree.
            is_maximizing (bool): True if the current player is maximizing their score, False for minimizing.

        Returns:
            tuple: A tuple containing the best score and the corresponding move.
        """

        if depth == 0 or self.is_winner(self.computer) or self.is_board_full():
            if self.is_winner(self.computer):
                return 1, None
            elif self.is_winner(self.player):
                return -1, None
            elif self.is_board_full():
                return 0, None

        if is_maximizing:
            best_score = -float('inf')
            best_move = None
            for move in range(9):
                if self.is_valid_move(move):
                    self.make_move(move, self.computer)
                    score, _ = self.minimax(depth - 1, False)
                    self.make_move(move, ' ')  # Undo the move
                    best_score = max(best_score, score)
                    if score > best_score:
                        best_move = move
            return best_score, best_move

        else:
            best_score = float('inf')
            best_move = None
            for move in range(9):
                if self.is_valid_move(move):
                    self.make_move(move, self.player)
                    score, _ = self.minimax(depth - 1, True)
                    self.make_move(move, ' ')  # Undo the move
                    best_score = min(best_score, score)
                    if score < best_score:
                        best_move = move
            return best_score, best_move

    def get_player_move(self):
        while True:
            move = input("Enter your move (1-9): ")
            try:
                move = int(move) - 1  # Convert to 0-based index
                if self.is_valid_move(move):
                    return move
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

    def computer_move(self):
        best_score, best_move = self.minimax(depth=2, is_maximizing=True)  # Adjust depth as needed
        self.make_move(best_move, self.computer)

    def play(self):
        print("Welcome to Tic Tac Toe!")

        # Ask if the user wants to go first
        first_move = input("Do you want to go first? (y/n): ").lower()
