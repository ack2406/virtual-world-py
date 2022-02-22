from vworld.Animal import Animal

import random


class CyberSheep(Animal):
    def __init__(self, position, world):
        super().__init__(11, 4, position, 'C', 'Cyber-Sheep', world)

    def giveBirth(self, position):
        return CyberSheep(position, self.world)

    def action(self):
        hogPosition = self.world.getClosestHogweed(self.position)
        if hogPosition:
            newPosition = self.world.getPositionClosestTo(self.position, hogPosition)
        else:
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
