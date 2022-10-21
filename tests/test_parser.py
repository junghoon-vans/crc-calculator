from argparse import Namespace

from src.crc_calculator.parser import parser


def test_parse_args():
    assert parser.parse_args(["100101", "101001010"]) == Namespace(
        polynomial='100101', data='101001010',
    )
