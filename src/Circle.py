from src.Figure import Figure
import math


class Circle(Figure):
    NAME = "Circle"

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimetr(self):
        return math.pi * self.radius * 2
