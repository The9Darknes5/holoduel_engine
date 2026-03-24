from holoduel_engine.engine.field import Field


class GameState:
    def __init__(self):
        self.field = Field()
        self.players = {}
        self.turn_player = None
        self.turn_count = 0

    def add_player(self, player):
        self.players[player.id] = player

    def start_game(self):
        if len(self.players) != 2:
            raise Exception("Game requires exactly 2 players")

        self.turn_player = 1
        self.turn_count = 1

    def next_turn(self):
        self.turn_player = 2 if self.turn_player == 1 else 1
        self.turn_count += 1