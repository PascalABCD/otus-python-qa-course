import pytest


class TestAddArea:
    def test_area_not_figure(self, create_circle):
        circle = create_circle
        with pytest.raises(ValueError):
            circle.add_area('triangle')

    def test_add_area_circle_circle(self, create_circle):
        circle = create_circle
        circle2 = create_circle
        assert round(circle.add_area(circle2), 1) == 169.8

    def test_add_area_circle_triangle(self, create_circle, create_triangle):
        circle = create_circle
        triangle = create_triangle
        assert round(circle.add_area(triangle), 1) == 90.9
