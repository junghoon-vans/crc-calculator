from typing import List

from crc_calculator.utils import convert_to_str


def calculate(polynomial: List[int], data: List[int]) -> str:
    """
        Args:
            polynomial: polynomial code
            data: input data
        Returns:
            reminder calculating polynomial and data
    """
    reminder = ""
    append_zeroes(polynomial, data)

    result = xor(polynomial, data)
    count = len(data) - len(polynomial)

    for i in range(count):
        result.pop(0)
        result.append(data[len(polynomial)+i])

        result = xor(
            polynomial if result[0] != 0 else [
                0 for _ in range(len(polynomial))
            ], result,
        )

        if i == count-1:
            result.pop(0)
            reminder = convert_to_str(result)
    return reminder


def append_zeroes(polynomial: List[int], data: List[int]):
    """Append zeroes to the data by the length of the polynomial"""
    result_length = len(polynomial) - 1
    for i in range(result_length):
        data.append(0)


def xor(a: List[int], b: List[int]) -> List[int]:
    """Calculate xor between int list"""
    result = []

    for i in range(len(a)):
        result.append(a[i] ^ b[i])

    return result
