from random import randint

class SnakesAndLadders:
    LADDERS = {
        1: 38,
        4: 14,
        9: 31,
        21: 42,
        28: 84,
        51: 67,
        72: 91,
        80: 99,
    }
    SNAKES = {
        17: 7,
        54: 34,
        64: 60,
        62: 19,
        87: 36,
        93: 73,
        95: 75,
        98: 79,
    }
    LAST_TILE = 100

    def __init__(self, n_players, verbose=False):
        self.n_players = n_players
        self.verbose = verbose
        self.players = [0] * n_players
        self.turn = 0
        self.winner = None  # determines if game is over
        self.dice_rolls = [0] * n_players

    def dice_roll(self):
        return randint(1, 6)

    def move_player(self, player_i):
        roll = self.dice_roll()
        # Stores the dice roll result
        self.dice_rolls[player_i] = roll  
        prev_pos = self.players[player_i]
        new_pos = prev_pos + roll

        if new_pos >= self.LAST_TILE:
            self.winner = player_i
            new_pos = self.LAST_TILE
        elif new_pos in self.SNAKES:
            new_pos = self.SNAKES[new_pos]
        elif new_pos in self.LADDERS:
            new_pos = self.LADDERS[new_pos]

        self.players[player_i] = new_pos

    def move_players(self):
        for player_i in range(self.n_players):
            self.move_player(player_i)
            if self.winner is not None:
                break

    def play_game(self):
        while self.winner is None:
            self.turn += 1
            self.move_players()
            if self.verbose:
                self.print_turn()
        return f"Player {self.winner + 1} Wins!"

    def print_turn(self):
        print(f"Turn {self.turn}:")
        # sort players by position
        pos_and_player_i = sorted(((pos, player_i) for player_i, pos in enumerate(self.players)), reverse=True)

        # print players with position
        player_pos_str = ' | '.join([f"({player_i + 1}) {pos} (rolled {self.dice_rolls[player_i]})" for pos, player_i in pos_and_player_i])
        print(player_pos_str)


game = SnakesAndLadders(n_players=2, verbose=True)
result = game.play_game()
print(result)


print("Final positions:", game.players)








