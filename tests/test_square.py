import pytest

from src.Square import Square


class TestSquare:
    def test_negative_side(self):
        with pytest.raises(ValueError):
            Square(-3)

    def test_invalid_side_type(self):
        with pytest.raises(TypeError):
            Square('a')

    def test_area(self, create_square):
        square = create_square
        assert square.area == 36

    def test_perimeter(self, create_square):
        square = create_square
        assert square.perimeter == 24
