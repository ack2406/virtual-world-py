from vworld.Plant import Plant


class SowThistle(Plant):
    def __init__(self, position, world):
        super().__init__(0, position, '*', 'Sow thistle', world)

    def giveBirth(self, position):
        return SowThistle(position, self.world)

    def reproduce(self):
        for _ in range(3):
            super().reproduce()
