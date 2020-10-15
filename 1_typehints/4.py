from typing import Any


# As a last resort, use Any to match everything
def greet(input_object: Any):
    print(input_object.greeting_fn())


# Not sure how to show this well, but there are cases when objects are not really typed
# but have fields / methods whose return types are needed and maybe known (tensorflow...)
class Unknown:
    def __init__(self, state: str):
        self.state = state

    def greeting_fn(self) -> str:
        return f"Hello. The state is: {self.state}"


if __name__ == "__main__":
    some_object_with_shady_past = Unknown("unknown")
    greet(some_object_with_shady_past)
