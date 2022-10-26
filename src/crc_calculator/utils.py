from typing import List


def convert_to_list(value: int) -> List[int]:
    """Convert int value to list

        Args:
            value: Integer value
        Returns:
            List of integer values decomposed by digits

    """
    return [int(i) for i in str(value)]


def convert_to_str(value: List[int]) -> str:
    """Convert int list to int

        Args:
            value: List consisting of integer
        Returns
            String value combined list of integer elements

    """
    s = [str(i) for i in value]
    res = "".join(s)
    return res
