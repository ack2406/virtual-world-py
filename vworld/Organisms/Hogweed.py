from vworld.Plant import Plant
from vworld.Animal import Animal
from vworld.Organisms.CyberSheep import CyberSheep


class Hogweed(Plant):
    def __init__(self, position, world):
        super().__init__(10, position, '$', 'Sosnowsky\'s hogweed', world)

    def giveBirth(self, position):
        return Hogweed(position, self.world)

    def action(self):
        positions = self.world.getNeighboringPositions(self.position)
        for position in positions:
            organism = self.world.getOrganismFromPosition(position)
            if isinstance(organism, Animal) and not isinstance(organism, CyberSheep):
                if not organism.immortality > 0:
                    self.world.organisms.pop(self.world.organisms.index(organism))
                    self.world.events.append(f'{organism.name} died from deadly poison of {self.name}.')
                else:
                    self.world.events.append(f'{organism.name} is immune to {self.name} thanks to immortality.')
        super().action()

    def attack(self, other):
        if self.strength > other.strength:
            if other.immortality > 0:
                self.world.events.append(f'{self.name} didn\'t do anything to {other.name}, \
                                because {other.name} is immortal.')
            else:
                self.world.organisms.pop(self.world.organisms.index(other))
                self.world.events.append(f'{other.name} died from deadly {self.name}.')
        else:
            self.world.events.append(f'{other.name} ate {self.name} like it was a normal grass.')

        self.world.organisms.pop(self.world.organisms.index(self))
        return True
