from vworld.Animal import Animal


class Wolf(Animal):
    def __init__(self, position, world):
        super().__init__(9, 5, position, 'W', 'Wolf', world)

    def giveBirth(self, position):
        return Wolf(position, self.world)
