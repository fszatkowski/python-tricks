import argparse
from dataclasses import dataclass


# We can improve commandline parsing if we wrap args with a dataclass
@dataclass
class Args:
    input: str
    output: str


# Standard commandline parsing using argparse.ArgumentParser requires writing a lot of code
def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-o", "--output", type=str, required=True)
    return Args(**parser.parse_args().__dict__)


if __name__ == '__main__':
    # Now IDE hints the fields and checks types
    args = parse_args()
    print(args)
    input_path: int = args.input
