"""Module for handling cli options"""
from argparse import ArgumentParser

from . import __version__


parser = ArgumentParser()

parser.add_argument(
    "polynomial",
    type=str,
)
parser.add_argument(
    "data",
    type=str,
)
parser.add_argument(
    "-V",
    "--version",
    action='version',
    version=f'crc-calculator {__version__}',
)
