"""Command-line implementation of crc-calculator"""
from typing import List
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

    polynomial = int(parser.get_polynomial())
    data = int(parser.get_data())

    calculate(
        polynomial=list_from(polynomial),
        data=list_from(data),
    )


def list_from(value: int) -> List[int]:
    """Make list from int value

        Args:
            value: int value to make list

    """
    return [int(p) for p in str(value)]
