class Card:
    def __init__(self, name):
        self.name = name
        self.owner = None
        self.current_zone = None

        self.triggers = [] 