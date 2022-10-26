"""Command-line implementation of crc-calculator"""
import sys
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
    parser.parse(argv or sys.argv[1:])

    polynomial = parser.get_polynomial().lstrip('0')
    data = parser.get_data().lstrip('0')

    checksum = calculate(
        polynomial=convert_to_list(polynomial),
        data=convert_to_list(data),
    )

    validation = calculate(
        polynomial=convert_to_list(polynomial),
        data=convert_to_list(data+checksum),
    )

    print(f'checksum: {checksum}')
    print(f'validation: {validation}')
