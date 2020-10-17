import abc

# ABC (abstract base classes) package provides tools for creating abstract classes and methods in python
# Abstract classes must inherit from abc.ABC class
# Then @abd.abstractmethod can be defined


class BaseClass(abc.ABC):
    @abc.abstractmethod
    def greet(self):
        pass

    # Abstract class can have non-abstract methods
    def base_greet(self):
        print("This is a greeting from the parent")


# Now subclass must implement greet
class SubClass(BaseClass):
    def greet(self):
        self.base_greet()
        print("Hello")


if __name__ == "__main__":
    # Try to instantiate base class
    try:
        base = BaseClass()
    except Exception as e:
        print(e)

    sub = SubClass()
    sub.greet()

    # Try inheriting from base class without overriding greet()
    try:

        class AnotherSubClass(BaseClass):
            pass

        another = AnotherSubClass()
    except Exception as e:
        print(e)
