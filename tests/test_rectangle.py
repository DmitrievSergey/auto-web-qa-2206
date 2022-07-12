def test_calculate_area(rectangle):
    assert rectangle.area == rectangle.first_side * rectangle.second_side


def test_calculate_perimetr(rectangle):
    assert rectangle.perimetr == rectangle.first_side * 2 + rectangle.second_side * 2


def test_add_area(rectangle, correct_triangle):
    assert rectangle.add_area(correct_triangle) == rectangle.area + correct_triangle.area
