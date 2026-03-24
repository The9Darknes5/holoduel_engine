class ChainSystem:
    def __init__(self):
        self.chain = []

    def add_to_chain(self, effect):
        self.chain.append(effect)

    def resolve(self):
        print("Resolviendo cadena...")

        while self.chain:
            effect = self.chain.pop()
            effect()