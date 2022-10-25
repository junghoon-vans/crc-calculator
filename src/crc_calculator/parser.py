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
        return self.args.polynomial

    def get_data(self) -> str:
        """Returns data

            Returns:
                data

        """
        return self.args.data
