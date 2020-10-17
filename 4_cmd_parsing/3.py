import click


# We can also use click package for commandline parsing
# Attaching parser to function is as simple as adding @click.command() and @click.options() decorators
# Commandline argument names must match function parameters
@click.command()
@click.option("-i", "--input_path", type=str, required=True)
@click.option("-o", "--output_path", type=str, required=True)
def main(input_path: str, output_path: str):
    print(input_path, output_path)


if __name__ == '__main__':
    main()
