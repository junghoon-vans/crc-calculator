"""Command-line implementation of crc-calculator"""
from typing import Optional
from typing import Sequence

from crc_calculator.calculator import calculate
from crc_calculator.parser import Parser
from crc_calculator.utils import convert_to_list


def main(argv: Optional[Sequence[str]] = None):
    """Main function to calculate crc.

        Args:
            argv: Arguments vector

    """
    parser = Parser()
    parser.parse(argv)

    polynomial = int(parser.get_polynomial())
    data = int(parser.get_data())

    result = calculate(
        polynomial=convert_to_list(polynomial),
        data=convert_to_list(data),
    )
    print(result)
