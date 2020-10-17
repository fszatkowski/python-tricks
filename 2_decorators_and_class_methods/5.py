# @classmethod decorator works similarly to @staticmethod, but also accepts class as an argument
# so it can be used to create factory methods
# both staticmethods and classmethods are inherited


class Baseclass:
    def __init__(self, name):
        self.name = name

    @classmethod
    def greet(cls):
        print(f"Hello, I am {cls.__name__}")

    # Sometimes we might want to create objects in a different way, and class method is a good way to do it
    @classmethod
    def from_input(cls):
        return cls(input())

    def __repr__(self):
        return f"Baseclass(name={self.name})"


class Subclass(Baseclass):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f"Subclass(name={self.name})"


if __name__ == "__main__":
    # Subclass inherits greet from Baseclass, but it's classmethod so it knows it's class (staticmethods don't)
    Baseclass.greet()
    Subclass.greet()

    # Subclass inherits factory method (but requires some work to make it work)
    instance = Baseclass.from_input()
    print(instance)
    sub_instance = Subclass.from_input()
    print(sub_instance)
