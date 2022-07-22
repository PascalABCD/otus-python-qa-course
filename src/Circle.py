import math
from src.Figure import Figure

PI = 3.14


class Circle(Figure):
    name = "Circle"

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius should be positive")

        self.radius = radius

    @property
    def area(self):
        return math.pow(self.radius, 2) * PI

    @property
    def perimeter(self):
        return self.radius * 2 * PI
