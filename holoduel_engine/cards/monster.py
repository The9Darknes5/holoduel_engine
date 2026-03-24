from holoduel_engine.cards.card import Card


class Monster(Card):
    def __init__(self, name, attack, defense):
        super().__init__(name)
        self.attack = attack
        self.defense = defense