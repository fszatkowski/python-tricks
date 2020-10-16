from typing import Callable


# Decorator is a function which takes other function as an argument
def decorator(fn: Callable) -> Callable:
    def wrapper():
        print("Decorator works.")
        fn()

    return wrapper


# If the wrapped function has any parameters, wrapper must take those into account
# Decorators can do anything with the function - eg. it is possible to write decorator that discards decorated function
def decorator_with_args(fn: Callable):
    def wrapper(*args, **kwargs):
        print(f"Passed arguments: {args}, {kwargs}")
        fn(*args, **kwargs)

    return wrapper


@decorator
def greeting_fn():
    print("Hello")


@decorator_with_args
def greeting_fn_with_args(name, *args, **kwargs):
    print(f"Hello {name}")


if __name__ == "__main__":
    greeting_fn()
    greeting_fn_with_args("Filip", 1, 2)
    greeting_fn_with_args("Filip", kwarg1=1, kwarg2=2)
    greeting_fn_with_args(name="Filip", kwarg1=1, kwarg2=2)