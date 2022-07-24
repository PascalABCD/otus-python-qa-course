import pytest

from homework2.src.Circle import Circle
from homework2.src.Triangle import Triangle
from homework2.src.Square import Square
from homework2.src.Rectangle import Rectangle


@pytest.fixture()
def create_circle():
    return Circle(5.2)


@pytest.fixture()
def create_triangle():
    return Triangle(3, 4, 5)


@pytest.fixture()
def create_square():
    return Square(6)


@pytest.fixture()
def create_rectangle():
    return Rectangle(6, 5)
