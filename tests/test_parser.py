import pytest

from src.crc_calculator.parser import Parser


@pytest.fixture(scope="module")
def parser() -> Parser:
    parser = Parser()
    parser.parse(["100101", "101001010"])
    return parser


def test_get_data(parser: Parser):
    assert parser.get_data() == '101001010'


def test_get_polynomial(parser: Parser):
    assert parser.get_polynomial() == '100101'
