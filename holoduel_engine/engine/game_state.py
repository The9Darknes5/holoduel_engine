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

    def summon_monster(self, player_id, monster):
        player_field = self.field.get_player_field(player_id)

        # Buscar zona libre
        for zone in player_field.main_monster_zones:
            if zone.is_empty():
                zone.place_card(monster)
                print(f"{monster.name} fue invocado en el campo")
                return True

        raise Exception("No hay zonas de monstruo disponibles")