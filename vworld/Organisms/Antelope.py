from vworld.Animal import Animal
import random


class Antelope(Animal):
    def __init__(self, position, world):
        super().__init__(4, 4, position, 'A', 'Antelope', world)

    def giveBirth(self, position):
        return Antelope(position, self.world)

    def action(self):
        newPosition = random.choice(self.world.getNeighboringJumpingPositions(self.position))

        otherOrganism = self.world.getOrganismFromPosition(newPosition)
        if otherOrganism:
            if type(self) is type(otherOrganism):
                self.reproduce()
            else:
                if otherOrganism.attack(self):
                    self.position = newPosition
        else:
            self.position = newPosition

    def attack(self, other):
        if random.randrange(0, 1):
            newPosition = random.choice(self.world.getFreePositions(self.position))
            self.position = newPosition
            self.world.events.append(f'{self.name} escaped from {other.name}.')
            return True
        else:
            return super().attack(other)
