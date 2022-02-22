from vworld.Organism import Organism
import random


class Animal(Organism):
    def __init__(self, strength, initiative, position, symbol, name, world):
        super().__init__(strength, initiative, position, symbol, name, world)

    def action(self):
        newPosition = random.choice(self.world.getNeighboringPositions(self.position))

        otherOrganism = self.world.getOrganismFromPosition(newPosition)
        if otherOrganism:
            if type(self) is type(otherOrganism):
                self.reproduce()
            else:
                if otherOrganism.attack(self):
                    self.position = newPosition
        else:
            self.position = newPosition
