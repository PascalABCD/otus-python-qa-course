import pytest

from homework2.src.Triangle import Triangle


class TestTriangle:
    def test_negative_side(self):
        with pytest.raises(ValueError):
            Triangle(-3, 4, 5)

    def test_invalid_side(self):
        with pytest.raises(ValueError):
            Triangle(1, 2, 3)

    def test_invalid_side_type(self):
        with pytest.raises(TypeError):
            Triangle('a', 2, 3)

    def test_area(self, create_triangle):
        triangle = create_triangle
        assert triangle.area == 6

    def test_perimeter(self, create_triangle):
        triangle = create_triangle
        assert triangle.perimeter == 12
