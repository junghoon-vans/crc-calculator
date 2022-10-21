"""Command-line implementation of crc-calculator"""
from typing import Optional
from typing import Sequence

from crc_calculator.parser import parser


def main(argv: Optional[Sequence[str]] = None):
    """Main function to run application

        Args:
            argv: Arguments vector

    """
    args = parser.parse_args(args=argv)
    print(args)
