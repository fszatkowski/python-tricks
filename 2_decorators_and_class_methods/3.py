# @property can also be used to simulate encapsulation in a weird way


class EncapsulatedClass:
    def __init__(self, public_field: int, private_field: int):
        self._public = public_field
        self._private = private_field

    @property
    def public(self) -> int:
        return self._public

    @public.setter
    def public(self, value: int):
        if value > 0:
            self._public = value
        else:
            raise ValueError("Value must be positive")


if __name__ == "__main__":
    enc = EncapsulatedClass(10, 100)
    # Private field can still be accessed but it's highlighted
    print(enc._private)
    # Public field accessed through getter is cool
    print(enc.public)
