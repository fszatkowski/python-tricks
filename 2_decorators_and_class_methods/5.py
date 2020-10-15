# @staticmethod decorator bounds method to class, not to an instance
# essentially it just binds a function to class namespace


class Rectangle:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    # This is just an example for educational purposes, this code overly complicated and don't write like this
    def area(self):
        return Rectangle._area(self.a, self.b)

    @staticmethod
    def _area(a: int, b: int) -> int:
        return a * b


if __name__ == "__main__":
    rectangle = Rectangle(1, 2)
    print(rectangle.area())

    # static method is equal to binding function to class
    Rectangle._area = lambda a, b: (a ** a + b ** b) ** 0.5
    print(rectangle.area())
