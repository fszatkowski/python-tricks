# To use type hinting, just specify type after variable declaration with semicolon

from typing import Callable, List

x: int = 5
text: str = "Hello"

# In Python versions < 3.9 only primitives such as int, str and float and classes are supported,
# so for hinting lists, functions etc we need to import from typing module

primes: List = [2, 3, 5, 7, 11]
sgn: Callable = lambda x: 0 if x == 0 else (1 if x > 0 else -1)

# We can be more specific with type hints using square brackets

evens: List[int] = [0, 2, 4, 6, 8, 10]
a_larger_than_b: Callable[[int, int], bool] = lambda a, b: a > b

# Then IDE can be used to better check our code
# eg. we it can statically check if our code is problematic

# This is not highlighted because we only specify outermost type
primes.append("This is not a number")
try:
    sgn([4, 6, 8])
except Exception as e:
    print(f"Execution error: {e}")

# But if we specified types, IDE can now check for problematic code
evens.append(1.1)

# In case of functions IDE is not smart enough, but mypy should work
try:
    a_larger_than_b("Number", 1.0)
except Exception as e:
    print((f"Execution error: {e}"))
