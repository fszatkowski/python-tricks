from typing import List, Optional, Union


# Type hints can be used for functions / methods
def naive_tokenize(string: str) -> List[str]:
    return string.split(" ")


# We can also specify optional parameters with type hints
def p_norm(vector: List[Union[float, int]], p: Optional[int] = None):
    if p is None:
        return sum([abs(x) for x in vector])
    else:
        return sum([abs(x) ** p for x in vector]) ** (1 / p)


# Can also define aliases
Vector = List[Union[float, int]]


def normalize(vector: Vector) -> Vector:
    norm_2 = p_norm(vector, p=2)
    return [v / norm_2 for v in vector]


if __name__ == "__main__":
    print(naive_tokenize("This is a sample sentence"))
    print(p_norm([1, 2, 3, 4]))
    print(p_norm([1, 2, 3, 4], p=2))
    print(normalize([1, 2, 3, 4]))
