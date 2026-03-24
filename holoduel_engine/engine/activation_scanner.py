class ActivationScanner:
    def __init__(self, game_state):
        self.game_state = game_state

    def scan(self, player_id):
        activatable_cards = []

        field = self.game_state.field
        player_field = field.get_player_field(player_id)

        # Revisar monstruos en campo
        for zone in player_field.main_monster_zones:
            if not zone.is_empty():
                card = zone.card

                # 🔥 placeholder para lógica futura
                if hasattr(card, "can_activate") and card.can_activate(self.game_state):
                    activatable_cards.append(card)

        return activatable_cards