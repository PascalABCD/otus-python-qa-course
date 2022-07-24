from homework2.src.Figure import Figure


class Rectangle(Figure):
    name = "Rectangle"

    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Side values should be positive")

        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return self.length * 2 + self.width * 2
