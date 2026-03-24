class Trigger:
    def __init__(self, event_name, condition, effect):
        self.event_name = event_name
        self.condition = condition
        self.effect = effect

    def check_and_activate(self, game_state, event_data):
        if self.condition(game_state, event_data): 
            # EN VEZ DE EJECUTAR → AGREGAR A CADENA
            game_state.chain_system.add_to_chain(
            lambda: self.effect(game_state, event_data)
        )