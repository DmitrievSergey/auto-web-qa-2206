def test_calculate_area(square):
    assert square.area == square.first_side ** 2


def test_calculate_perimetr(square):
    assert square.perimetr == square.first_side * 4


def test_add_area(square, correct_triangle):
    assert square.add_area(correct_triangle) == square.area + correct_triangle.area
