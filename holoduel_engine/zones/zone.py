class Zone:
    def __init__(self):
        self.card = None

    def is_empty(self):
        return self.card is None

    def place_card(self, card):
        if not self.is_empty():
            raise Exception("Zone is occupied")

        self.card = card
        card.current_zone = self

    def remove_card(self):
        card = self.card
        self.card = None

        if card:
            card.current_zone = None

        return card