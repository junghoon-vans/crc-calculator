"""Command-line implementation of crc-calculator"""
from typing import Optional
from typing import Sequence

from crc_calculator.calculator import calculate
from crc_calculator.parser import Parser


def main(argv: Optional[Sequence[str]] = None):
    """Main function to run application

        Args:
            argv: Arguments vector

    """
    parser = Parser()
    parser.parse(argv)

    calculate(
        polynomial=list(parser.get_polynomial()),
        data=list(parser.get_data()),
    )
