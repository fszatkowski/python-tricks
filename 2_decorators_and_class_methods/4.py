# @property is a descriptor
# Descriptors are objects implementing methods from descriptor protocol:
# - __get__(self, obj, type=None) -> object
# - __set__(self, obj, value) -> None
# - __delete__(self, obj) -> None
# If only the first one is implemented, then it's non data-descriptor,
# If the others are implemented then it's data descriptor


class PositiveInt(object):
    def __init__(self, value=None):
        if value is None or value > 0:
            self._value = value
        else:
            raise ValueError(f"Cannot set value: {value}. Only positive values allowed")

    def __get__(self, instance, cls):
        if self._value is not None:
            return self._value
        else:
            raise ValueError("Value not set")

    def __set__(self, instance, value):
        if value > 0:
            self._value = value
        else:
            raise ValueError(
                f"Cannot set value: {self._value}. Only positive values allowed"
            )

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return str(self)


# To use descriptors, they have to be class attributes, not instance attributes
# Then we can parametrize whole classes
class PositiveIntContainer:
    x = PositiveInt(1)
    y = PositiveInt(3)
    z = PositiveInt()


if __name__ == "__main__":
    container = PositiveIntContainer()

    # Descriptor protocol allows dotted access here
    print(f"X equals: {container.x}")

    # We can also change value with provided security
    container.x = 12345
    print(f"X equals: {container.x}")

    try:
        container.y = -5
    except Exception as e:
        print(e)
    print(f"Y equals: {container.y}")

    # Unset items cannot be accessed
    try:
        print(container.z)
    except Exception as e:
        print(e)
    container.z = 5
    print(f"Z equals: {container.z}")

    # Allows for global change of all items in class with implemented security
    PositiveIntContainer.x = 5
    print(f"X equals: {container.x}")
