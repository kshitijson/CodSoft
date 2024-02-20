import random


class SmartComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # Choose a random corner for the first move
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)["position"]
        return square

    def minimax(self, state, player):
        max_player = self.letter  # AI player
        other_player = "O" if player == "X" else "X"

        if state.current_winner == other_player:
            return {"position": None, "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            # Each score should maximize
            best = {"position": None, "score": -float("inf")}
        else:
            # Each score should minimize
            best = {"position": None, "score": float("inf")}

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            # Simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            # Undo the move
            state.board[possible_move] = " "
            state.current_winner = None
            # this represents the move optimal next move
            sim_score["position"] = possible_move
            if player == max_player:  # Maximizing player
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:  # Minimizing player
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best
