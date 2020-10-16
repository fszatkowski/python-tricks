# @property is a descriptor
# Descriptors are objects implementing methods from descriptor protocol:
# - __get__(self, obj, type=None) -> object
# - __set__(self, obj, value) -> None
# - __delete__(self, obj) -> None


# Lets create descriptor object
class PositiveInt:
    # Using name allows us to access instance attributes
    def __init__(self, name: str):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(value, int) and value > 0:
            instance.__dict__[self.name] = value
        else:
            raise ValueError(
                f"Cannot set value: {value}. Only positive values allowed"
            )


# To use descriptors, they have to be class attributes, not instance attributes
# Descriptors can be also used to define class constants
class PositiveVector:
    x = PositiveInt("x")
    y = PositiveInt("y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return str(self)


if __name__ == "__main__":
    # Create vector
    v1 = PositiveVector(1, 5)
    print(f"v1: {v1}")

    # Create second one and check if v1 was affected
    v2 = PositiveVector(2, 3)
    print(f"v1: {v1}")
    print(f"v2: {v2}")

    # Try to change values
    try:
        v1.x = 2
        v1.y = -2
    except Exception as e:
        print(e)
