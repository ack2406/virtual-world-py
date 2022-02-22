from vworld.Plant import Plant


class Guarana(Plant):
    def __init__(self, position, world):
        super().__init__(0, position, 'G', 'Guarana', world)

    def giveBirth(self, position):
        return Guarana(position, self.world)

    def attack(self, other):
        self.world.organisms.pop(self.world.organisms.index(self))
        other.strength += 3
        self.world.events.append(f'Strength of {other.name} increased by eating {self.name}.')
        return True
