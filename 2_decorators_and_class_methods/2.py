# @property decorator
# Function decorated wih @property defines class field
# This is useful when some attributes are dependent on each other


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self) -> float:
        return 3.14 * self.radius * self.radius

    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Negative area provided")
        self.radius = (value / 3.14) ** 0.5

    @area.deleter
    def area(self):
        del self.radius

    def __str__(self) -> str:
        if hasattr(self, "radius"):
            return f"Circle with radius {self.radius}."
        else:
            return "Empty circle"


if __name__ == "__main__":
    circle = Circle(5)
    print(circle)
    print(circle.area)
    circle.area = 25
    print(circle)
    del circle.area
    print(circle)
