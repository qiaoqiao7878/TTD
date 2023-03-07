import sys


class Argument:
    def __init__(self, argv) -> None:
        self.python_file_name = argv[1]
        self.function_name = argv[2]
        self.source_file = argv[3]
        self.destination_file = argv[4]


def parse_arguments(argv):
    if len(argv) != 5:
        raise ValueError
    return Argument(argv)


if __name__ == "__main__":
    argument = parse_arguments(sys.argv)
