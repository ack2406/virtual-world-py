from vworld.Plant import Plant


class Belladonna(Plant):
    def __init__(self, position, world):
        super().__init__(99, position, 'B', 'Belladonna', world)

    def giveBirth(self, position):
        return Belladonna(position, self.world)

    def attack(self, other):
        if self.strength > other.strength:
            if other.immortality > 0:
                self.world.events.append(f'{self.name} didn\'t do anything to {other.name}, \
                                because {other.name} is immortal.')
            else:
                self.world.organisms.pop(self.world.organisms.index(other))
                self.world.events.append(f'{other.name} died to deadly {self.name}.')

        self.world.organisms.pop(self.world.organisms.index(self))
        return True
