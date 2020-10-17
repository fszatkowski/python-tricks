import argparse


# Standard commandline parsing using argparse.ArgumentParser requires writing a lot of code
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-o", "--output", type=str, required=True)
    return parser.parse_args()


if __name__ == '__main__':
    # argparse.Namespace returned by parser is a blackbox - we can't use hints, check for types, typos
    args = parse_args()
    print(args)
