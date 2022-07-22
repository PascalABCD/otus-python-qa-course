import pytest

from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square
from src.Rectangle import Rectangle


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
