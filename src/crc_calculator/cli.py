"""Command-line implementation of crc-calculator"""
from typing import Optional
from typing import Sequence

from crc_calculator.parser import Parser


def main(argv: Optional[Sequence[str]] = None):
    """Main function to run application

        Args:
            argv: Arguments vector

    """
    parser = Parser()
    parser.parse(argv)

    print(parser.get_polynomial())
    print(parser.get_data())
