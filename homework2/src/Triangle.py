import math
from homework2.src.Figure import Figure


class Triangle(Figure):
    name = "Triangle"

    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Side values should be positive")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle doesn't exist")

        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
