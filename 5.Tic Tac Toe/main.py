import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]
        self.current_winner = None

    def print_board(self):
        print("\n")
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def available_moves(self):
        return [(i, j) for i in range(3) for j in range(3)
                if self.board[i][j] not in ['X', 'O']]

    def empty_squares(self):
        return any(cell not in ['X', 'O'] for row in self.board for cell in row)

    def make_move(self, i, j, letter):
        if self.board[i][j] not in ['X', 'O']:
            self.board[i][j] = letter
            if self.winner(i, j, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, row, col, letter):
        # Check row
        row_win = True
        for c in range(3):
            if self.board[row][c] != letter:
                row_win = False
                break
        if row_win:
            return True

        # Check column
        col_win = True
        for r in range(3):
            if self.board[r][col] != letter:
                col_win = False
                break
        if col_win:
            return True

        # Check diagnals
        if row == col:
            diag_win = True
            for i in range(3):
                if self.board[i][i] != letter:
                    diag_win = False
                    break
            if diag_win:
                return True

        if row + col == 2:
            diag2_win = True
            for i in range(3):
                if self.board[i][2 - i] != letter:
                    diag2_win = False
                    break
            if diag2_win:
                return True

        return False


class Player:
    def __init__(self, letter):
        self.letter = letter  

    def get_move(self, game: TicTacToe):
        pass  # method override


class HumanPlayer(Player):
    def get_move(self, game: TicTacToe):
        valid = False
        move = None

        while not valid:
            try:
                val = int(input(f'Player {self.letter}, enter your move (1-9): '))
                if val < 1 or val > 9:
                    print("Please enter a number between 1 and 9.")
                    continue
                row, col = (val - 1) // 3, (val - 1) % 3
                if (row, col) in game.available_moves():
                    valid = True
                    move = (row, col)
                else:
                    print("That spot is already taken.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
        return move


class ComputerPlayer(Player):
    def get_move(self, game: TicTacToe):
        if len(game.available_moves()) == 9:
            return random.choice(game.available_moves())  # First move random
        return self.minimax(game, True)[1]

    def minimax(self, game: TicTacToe, is_maximizing):
        if game.current_winner == self.letter:
            return (1, None)
        elif game.current_winner == ('X' if self.letter == 'O' else 'O'):
            return (-1, None)
        elif not game.empty_squares():
            return (0, None)

        if is_maximizing:
            best = (-math.inf, None)
            for move in game.available_moves():
                i, j = move
                game.make_move(i, j, self.letter)
                score = self.minimax(game, False)[0]
                game.board[i][j] = str(i * 3 + j + 1)  # Undo move
                game.current_winner = None
                if score > best[0]:
                    best = (score, move)
            return best
        else:
            opponent = 'X' if self.letter == 'O' else 'O'
            best = (math.inf, None)
            for move in game.available_moves():
                i, j = move
                game.make_move(i, j, opponent)
                score = self.minimax(game, True)[0]
                game.board[i][j] = str(i * 3 + j + 1)  # Undo move
                game.current_winner = None
                if score < best[0]:
                    best = (score, move)
            return best


def play(game: TicTacToe, player_x: Player, player_o: Player):
    game.print_board()
    letter = 'X'

    while game.empty_squares():
        if letter == 'X':
            move = player_x.get_move(game)
        else:
            move = player_o.get_move(game)

        if move is None:
            print("No move returned. Exiting.")
            break

        i, j = move
        if game.make_move(i, j, letter):
            print(f"\n{letter} makes a move to ({i}, {j}):")
            game.print_board()

            if game.current_winner:
                print(f"{letter} wins! 🎉")
                return

            letter = 'O' if letter == 'X' else 'X'

    print("It is a draw.")


if __name__ == "__main__":
    game = TicTacToe()
    human = HumanPlayer('X')
    computer = ComputerPlayer('O')
    play(game, human, computer)
