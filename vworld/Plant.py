from vworld.Organism import Organism
import random


class Plant(Organism):
    def __init__(self, strength, position, symbol, name, world):
        super().__init__(strength, 0, position, symbol, name, world)

    def action(self):
        if not random.randrange(0, 10):
            self.reproduce()
