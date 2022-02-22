from vworld.Animal import Animal
import random


class Turtle(Animal):
    def __init__(self, position, world):
        super().__init__(2, 1, position, 'T', 'Turtle', world)

    def giveBirth(self, position):
        return Turtle(position, self.world)

    def action(self):
        if random.randrange(0, 4):
            super().action()

    def attack(self, other):
        if self.strength > other.strength:
            if other.immortality > 0:
                self.world.events.append(f'{self.name} tried to kill {other.name} in defense, \
                                but {other.name} is immortal.')
            else:
                self.world.events.append(f'{self.name} killed {other.name} in defense.')
                self.world.organisms.pop(self.world.organisms.index(other))
            return False

        if other.strength < 5:
            self.world.events.append(f'{self.name} reflected attack of {other.name}.')
            return False

        self.world.events.append(f'{other.name} attacked and killed {self.name}.')
        self.world.organisms.pop(self.world.organisms.index(self))
        return True
