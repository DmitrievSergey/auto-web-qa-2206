import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture
def correct_triangle():
    return Triangle(2, 2, 3)


@pytest.fixture
def incorrect_triangle():
    return Triangle(1, 2, 3)


@pytest.fixture
def rectangle():
    return Rectangle(4, 5)


@pytest.fixture
def square():
    return Square(4)


@pytest.fixture
def circle():
    return Circle(4)
