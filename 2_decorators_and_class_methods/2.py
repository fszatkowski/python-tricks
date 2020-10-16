# @property decorator
# Function decorated wih @property defines class field
# This is useful when some attributes are dependent on each other
# Or when we want to simulate encapsulation (although python discourage this if it's not necessary)
from typing import Callable


class Circle:
    # Declare private fields
    _radius: float
    _color: str
    _describe_fn: Callable

    def __init__(self, radius: float, color: str = ""):
        # Notice how setters are used here, so we handle cases like negative radius
        # But this hides the "real" fields with underscores
        self.radius = radius
        self._describe_fn = self.basic_desc
        # If color was provided, initialize the field
        if color:
            self.color = color

    # Define setter and getter for radius
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Negative radius not supported.")
        self._radius = value

    @property
    def area(self) -> float:
        return 3.14 * self._radius * self._radius

    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("Negative area provided")
        self._radius = (value / 3.14) ** 0.5

    # Define optional property color
    # Use getter to check if color field is present
    # Use setter and deleter to edit __str__ when color is added or removed
    @property
    def color(self) -> str:
        if hasattr(self, "_color"):
            return self._color
        else:
            return "No color"

    @color.setter
    def color(self, value):
        self._color = value
        self._describe_fn = self.extended_desc

    @color.deleter
    def color(self):
        del self._color
        self._describe_fn = self.basic_desc

    def describe(self):
        print(self._describe_fn())

    def basic_desc(self) -> str:
        return f"Circle(r={self.radius}, area={self.area})"

    def extended_desc(self) -> str:
        return f"Circle(r={self.radius}, area={self.area}, color={self.color})"


if __name__ == "__main__":
    # Init and show basic circle
    circle = Circle(5, "red")
    circle.describe()

    # Change area - setter changes radius as well
    print()
    circle.area = 25
    circle.describe()

    # Delete color - deleter swaps _describe_fn
    print()
    print(circle._describe_fn)
    del circle.color
    circle.describe()
    print(circle._describe_fn)
