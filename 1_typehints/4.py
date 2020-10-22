from typing import Any


# As a last resort, use Any to match everything
def greet(input_object: Any):
    print(input_object.greeting_fn())


# Not sure how to show this well, there are cases when objects are not really typed well
# but have fields / methods whose return types are needed and maybe known (tensorflow...)
class Unknown:
    def __init__(self, state: str):
        self.state: str = state

    def greeting_fn(self) -> str:
        return f"Hello. The state is: {self.state}"

    # Also, in python 3.7, if we want to hint class from inside the class, we need to use string
    # as a type as class name is not recognized from inside the class
    def copy(self) -> "Unknown":
        return Unknown(self.state)


if __name__ == "__main__":
    some_object_with_shady_past = Unknown("unknown")
    greet(some_object_with_shady_past)
