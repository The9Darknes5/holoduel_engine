from holoduel_engine.cards.card import Card
from holoduel_engine.effects.trigger import Trigger

class Monster(Card):
    def __init__(self, name, attack, defense):
        super().__init__(name)
        self.attack = attack
        self.defense = defense

        self.triggers.append(
            Trigger(
                "on_summon",
                lambda game_state, data: data["card"] == self,
                lambda game_state, data: print(f"{self.name} activó su efecto al ser invocado")
            )
        )

    def can_activate(self, game_state):
        return True