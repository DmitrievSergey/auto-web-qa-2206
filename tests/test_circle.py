import math


def test_calculate_area(circle):
    assert circle.area == math.pi * circle.radius ** 2


def test_calculate_perimetr(circle):
    assert circle.perimetr == 2 * math.pi * circle.radius


def test_add_area(circle, correct_triangle):
    assert circle.add_area(correct_triangle) == circle.area + correct_triangle.area
