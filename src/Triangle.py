import math

from src.Figure import Figure


class Triangle(Figure):
    NAME = "Triangle"

    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        if (self.first_side + self.second_side <= self.third_side) or (
                self.first_side + self.third_side <= self.second_side) or (
                self.third_side + self.second_side <= self.first_side):
            raise ValueError('wrong sides')

    @property
    def perimetr(self):
        return self.first_side + self.second_side + self.third_side

    @property
    def area(self):
        per = self.perimetr / 2
        return math.sqrt(per * (per - self.first_side) * (per - self.second_side)
                         * (per - self.third_side))
