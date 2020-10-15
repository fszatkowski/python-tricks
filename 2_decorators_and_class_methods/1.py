# Decorator is a function which takes other function as an argument
from typing import Callable


def decorator(fn: Callable) -> Callable:
    def wrapper():
        print("Decorator works.")
        fn()

    return wrapper


def decorator_with_args(fn: Callable):
    def wrapper(*args, **kwargs):
        print(f"Passed arguments: {args}, {kwargs}")
        fn(*args, **kwargs)

    return wrapper


@decorator
def greeting_fn():
    print("Hello")


@decorator_with_args
def greeting_fn_with_args(*args, **kwargs):
    print("Hello")


if __name__ == "__main__":
    greeting_fn()
    greeting_fn_with_args(1, 2, my_name="Filip")
