from typing import Dict, List, Union

# Type hints can be nested
languages: Dict[str, List[str]] = {
    "statically-typed": ["C++, Java"],
    "dynamically-typed": ["Python"],
}
languages_with_difficulty: Dict[str, List[Dict[str, str]]] = {
    "statically-typed": [{"C++": "hard", "Java": "easy"}],
    "dynamically-typed": [{"Python": "easy"}],
}

# With this ide show hints considering that we have lists as a values
languages_with_difficulty["dynamically-typed"]

# Also can be used for unions
my_lucky_numbers: List[Union[int, float]] = [0.0, 7]
