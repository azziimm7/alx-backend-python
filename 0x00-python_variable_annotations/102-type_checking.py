#!/usr/bin/env python3
"""
A module that defines a function that
returns a list repeated based on the factor variable
"""
from typing import Tuple, List, TYPE_CHECKING


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return the list repeated based on the factor variable"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


if (not TYPE_CHECKING):
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3.0)
