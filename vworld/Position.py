import math


class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def getDistance(self, other):
        return int(math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2))

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'({self.x}, {self.y})'
