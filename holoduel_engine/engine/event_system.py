class EventSystem:
    def __init__(self, game_state):
        self.game_state = game_state

    def dispatch(self, event_name, event_data):
        field = self.game_state.field

        for zone in field.get_all_zones():
            if not zone.is_empty():
                card = zone.card

                for trigger in card.triggers:
                    if trigger.event_name == event_name:
                        trigger.check_and_activate(self.game_state, event_data)