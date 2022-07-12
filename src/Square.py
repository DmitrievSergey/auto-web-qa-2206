from src.Figure import Figure


class Square(Figure):
    NAME = "Square"

    def __init__(self, first_side):
        self.first_side = first_side

    @property
    def area(self):
        return self.first_side**2

    @property
    def perimetr(self):
        return self.first_side * 4
