from src.Figure import Figure


class Rectangle(Figure):
    NAME = "Rectangle"

    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

    @property
    def area(self):
        return self.first_side * self.second_side

    @property
    def perimetr(self):
        return self.first_side * 2 + self.second_side * 2
