from vworld.Plant import Plant


class Grass(Plant):
    def __init__(self, position, world):
        super().__init__(0, position, '/', 'Grass', world)

    def giveBirth(self, position):
        return Grass(position, self.world)
