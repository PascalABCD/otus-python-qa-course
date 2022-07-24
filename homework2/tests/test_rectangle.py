import pytest

from homework2.src.Rectangle import Rectangle


class TestRectangle:
    def test_negative_side(self):
        with pytest.raises(ValueError):
            Rectangle(-3, 5)

    def test_invalid_side_type(self):
        with pytest.raises(TypeError):
            Rectangle('a', 5)

    def test_area(self, create_rectangle):
        rectangle = create_rectangle
        assert rectangle.area == 30

    def test_perimeter(self, create_rectangle):
        rectangle = create_rectangle
        assert rectangle.perimeter == 22
