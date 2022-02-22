from vworld.Animal import Animal
import random


class Fox(Animal):
    def __init__(self, position, world):
        super().__init__(3, 7, position, 'F', 'Fox', world)

    def giveBirth(self, position):
        return Fox(position, self.world)

    def action(self):
        neighboringPositions = self.world.getNeighboringPositions(self.position)
        safePositions = []
        for pos in neighboringPositions:
            if not self.world.getOrganismFromPosition(pos) \
                    or self.world.getOrganismFromPosition(pos).strength < self.strength:
                safePositions.append(pos)

        newPosition = random.choice(safePositions) if (len(safePositions)) else random.choice(neighboringPositions)

        otherOrganism = self.world.getOrganismFromPosition(newPosition)
        if otherOrganism:
            if type(self) is type(otherOrganism):
                self.reproduce()
            else:
                if otherOrganism.attack(self):
                    self.position = newPosition
        else:
            self.position = newPosition
