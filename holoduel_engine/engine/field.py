from holoduel_engine.zones.zone import Zone


class PlayerField:
    def __init__(self):
        self.main_monster_zones = [Zone() for _ in range(5)]
        self.spell_trap_zones = [Zone() for _ in range(5)]
        self.field_zone = Zone()
        self.pendulum_zones = [Zone(), Zone()]

    def get_all_zones(self):
        return (
            self.main_monster_zones +
            self.spell_trap_zones +
            [self.field_zone] +
            self.pendulum_zones
        )


class Field:
    def __init__(self):
        self.players = {
            1: PlayerField(),
            2: PlayerField()
        }

        self.extra_monster_zones = [Zone(), Zone()]

    def get_player_field(self, player_id):
        return self.players[player_id]

    def get_all_zones(self):
        zones = []

        for player_field in self.players.values():
            zones.extend(player_field.get_all_zones())

        zones.extend(self.extra_monster_zones)

        return zones