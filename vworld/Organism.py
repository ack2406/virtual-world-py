import random


class Organism:
    def __init__(self, strength, initiative, position, symbol, name, world):
        self._strength = strength
        self._initiative = initiative
        self._position = position
        self._symbol = symbol
        self._name = name
        self._world = world
        self._immortality = -5

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        self._strength = value

    @property
    def initiative(self):
        return self._initiative

    @initiative.setter
    def initiative(self, value):
        self._initiative = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def world(self):
        return self._world

    @world.setter
    def world(self, value):
        self._world = value

    @property
    def isAlive(self):
        return self._isAlive

    @isAlive.setter
    def isAlive(self, value):
        self._isAlive = value

    @property
    def immortality(self):
        return self._immortality

    @immortality.setter
    def immortality(self, value):
        self._immortality = value

    def action(self):
        pass

    def attack(self, other):
        if self.strength > other.strength:
            if other.immortality > 0:
                self.world.events.append(
                    f'{self.name} tried to kill {other.name} in defense, but {other.name} is immortal.')
            else:
                self.world.events.append(f'{self.name} killed {other.name} in defense.')
                self.world.organisms.pop(self.world.organisms.index(other))
            return False

        if self.immortality > 0:
            self.world.events.append(f'{other.name} attacked and tried to kill {self.name}, \
                            but {self.name} is immortal.')
            return False

        self.world.events.append(f'{other.name} attacked and killed {self.name}.')
        self.world.organisms.pop(self.world.organisms.index(self))
        return True

    def giveBirth(self, position):
        pass

    def reproduce(self):
        positions = self.world.getFreePositions(self.position)
        if len(positions):
            newPosition = random.choice(positions)
            newOrganism = self.giveBirth(newPosition)
            self.world.addOrganism(newOrganism)

    def __str__(self):
        return self._symbol
