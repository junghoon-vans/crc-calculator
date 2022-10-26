from typing import List


def calculate(polynomial: List[int], data: List[int]):
    result_length = len(polynomial) - 1
    for i in range(result_length):
        data.append(0)

    result = xor(polynomial, data)
    print(result)


def xor(a: List[int], b: List[int]) -> List[int]:
    """Calculate xor between int list"""
    result = []

    for i in range(len(a)):
        result.append(a[i] ^ b[i])

    return result
