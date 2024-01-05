#!/usr/bin/env python3
""" sum_list module
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ finds the sum of a list

    Args:
        input_list (typing.List[float]): list containing float values

    Returns:
        (float): sum of the input_list.
    """
    return sum(input_list)
