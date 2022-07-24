import math
from homework2.src.Figure import Figure


class Square(Figure):
    name = "Square"

    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side value should be positive")
        self.side = side

    @property
    def area(self):
        return math.pow(self.side, 2)

    @property
    def perimeter(self):
        return self.side * 4
