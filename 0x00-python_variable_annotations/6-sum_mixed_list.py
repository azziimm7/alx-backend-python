#!/usr/bin/env python3
""" A module define a function sums mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sums mixed list and return thier sum as float"""
    ans: float = 0
    for i in mxd_lst:
        ans += i
    return ans 
