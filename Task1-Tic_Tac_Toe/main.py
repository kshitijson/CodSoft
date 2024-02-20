from utils.HumanPlayer import HumanPlayer
from utils.SmartComputer import SmartComputerPlayer
from utils.TicTacToe import TicTacToe

# def play(game, x_player, o_player, print_game=True):
#     if print_game:
#         game.print_board_nums()

#     letter = "X"
#     while game.empty_squares():
#         if letter == "O":
#             square = o_player.get_move(game)
#         else:
#             square = x_player.get_move(game)

#         if game.make_move(square, letter):
#             if print_game:
#                 print(f"{letter} makes a move to square {square}")
#                 game.print_board()
#                 print("")  # Empty line

#             if game.current_winner:
#                 if print_game:
#                     print(letter + " wins!")
#                 return letter  # Ends the loop and exits the game
#             letter = "O" if letter == "X" else "X"  # Switch player

#         if print_game:
#             print("It's a tie!")


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")  # Empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter  # Ends the loop and exits the game
            letter = "O" if letter == "X" else "X"  # Switch player

    if print_game:
        print("It's a tie!")


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = SmartComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
