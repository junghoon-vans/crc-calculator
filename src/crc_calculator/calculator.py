from typing import List


def calculate(polynomial: List[int], data: List[int]) -> List[int]:
    crc: List[int] = []
    result_length = len(polynomial) - 1

    for i in range(result_length):
        data.append(0)

    result = xor(polynomial, data)
    count = len(data) - len(polynomial)

    for i in range(count):
        result.pop(0)
        result.append(data[len(polynomial)+i])

        if i == count-1:
            result.pop(0)
            crc = result
        else:
            result = xor(
                [0 for _ in range(len(polynomial))],
                result,
            ) if result[0] == 0 else xor(polynomial, result)

    return crc


def xor(a: List[int], b: List[int]) -> List[int]:
    """Calculate xor between int list"""
    result = []

    for i in range(len(a)):
        result.append(a[i] ^ b[i])

    return result
