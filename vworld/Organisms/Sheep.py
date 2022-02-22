from vworld.Animal import Animal


class Sheep(Animal):
    def __init__(self, position, world):
        super().__init__(4, 4, position, 'S', 'Sheep', world)

    def giveBirth(self, position):
        return Sheep(position, self.world)
