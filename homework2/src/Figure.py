class Figure:
    name = None

    @property
    def area(self):
        return None

    @property
    def perimeter(self):
        return None

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError
        return self.area + figure.area
