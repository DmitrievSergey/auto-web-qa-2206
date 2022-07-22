import math

import pytest

from src.Triangle import Triangle


def test_rise_error_wrong_side():
    with pytest.raises(ValueError) as err:
        Triangle(1, 1, 3)
        assert str(err.value) == 'wrong sides'


def test_calculate_perimetr(correct_triangle):
    assert correct_triangle.perimetr == correct_triangle.first_side + \
           correct_triangle.second_side + correct_triangle.third_side


def test_calculate_area(correct_triangle):
    per = correct_triangle.perimetr / 2
    assert correct_triangle.area == math.sqrt(
        per * (per - correct_triangle.first_side) * (per - correct_triangle.second_side)
        * (per - correct_triangle.third_side))


def test_add_area(circle, correct_triangle):
    assert correct_triangle.add_area(circle) == circle.area + correct_triangle.area
