# In Python 3.9 type hinting was improved and works out of the box without typing module
# eg. we can use list, dict, set etc. to hint without any imports


def naive_tokenize(string: str) -> list[str]:
    return string.split(" ")


# this is still a bit raw, eg. couldn't find a good way to annotate callable with parameter types
# also this syntax breaks program for earlier versions of python and is not understood by mypy
# so it's cool but let's not use it
tok_fn: callable = naive_tokenize
