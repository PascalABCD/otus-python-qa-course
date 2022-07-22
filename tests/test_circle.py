import pytest

from src.Circle import Circle


class TestCircle:
    def test_name(self):
        assert Circle.name == "Circle"

    def test_negative_radius(self):
        with pytest.raises(ValueError):
            Circle(-5)

    def test_invalid_radius_type(self):
        with pytest.raises(TypeError):
            Circle('three')

    def test_zero_radius(self):
        with pytest.raises(ValueError):
            Circle(0)

    def test_area(self, create_circle):
        circle = create_circle
        assert round(circle.area, 1) == 84.9

    def test_perimeter(self, create_circle):
        circle = create_circle
        assert round(circle.perimeter, 1) == 32.7
