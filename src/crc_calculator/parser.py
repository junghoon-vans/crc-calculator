"""Module for handling cli options"""
from argparse import ArgumentParser
from typing import Optional
from typing import Sequence

from . import __version__


class Parser:
    _parser = ArgumentParser()

    def __init__(self):
        self.args = None

        self._parser.add_argument(
            "polynomial",
            type=str,
        )
        self._parser.add_argument(
            "data",
            type=str,
        )
        self._parser.add_argument(
            "-V",
            "--version",
            action='version',
            version=f'crc-calculator {__version__}',
        )

    def parse(self, argv: Optional[Sequence[str]] = None) -> None:
        """Parse arguments vector

            Args:
                argv: Arguments vector

        """
        self.args = self._parser.parse_args(argv)

    def get_polynomial(self) -> str:
        """Returns polynomial

            Returns:
                polynomial

        """
        polynomial = self.args.polynomial
        validate(polynomial)
        return polynomial

    def get_data(self) -> str:
        """Returns data

            Returns:
                data

        """
        data = self.args.data
        validate(data)
        return data


def validate(value: str) -> None:
    """Check if value is binary.

        Args:
            value: Binary string

    """
    if not all(map(lambda x: x in ["0", "1"], list(value))):
        print("Please enter binary numbers only!")
        exit(0)
