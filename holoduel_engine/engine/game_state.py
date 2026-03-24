from holoduel_engine.engine.field import Field
from holoduel_engine.engine.activation_scanner import ActivationScanner
from holoduel_engine.engine.event_system import EventSystem
from holoduel_engine.engine.chain_system import ChainSystem

class GameState:
    def __init__(self):
        self.field = Field()
        self.players = {}
        self.turn_player = None
        self.turn_count = 0
        self.activation_scanner = ActivationScanner(self)
        self.event_system = EventSystem(self)
        self.chain_system = ChainSystem()

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
                self.event_system.dispatch("on_summon", {
                    "player_id": player_id,
                    "card": monster
                })
                
                self.chain_system.resolve()
                return True

        raise Exception("No hay zonas de monstruo disponibles")
    
    def get_activatable_cards(self, player_id):
        return self.activation_scanner.scan(player_id)