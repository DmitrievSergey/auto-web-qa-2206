class Figure:
    NAME = None

    @property
    def area(self) -> int:
        pass

    @property
    def perimetr(self) -> int:
        pass

    def add_area(self, figure):
        return self.area + figure.area
