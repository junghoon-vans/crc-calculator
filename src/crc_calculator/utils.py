from typing import List


def convert_to_list(value: int) -> List[int]:
    """Convert int value to list

        Args:
            value: Integer value
        Returns:
            List of integer values decomposed by digits

    """
    return [int(i) for i in str(value)]
