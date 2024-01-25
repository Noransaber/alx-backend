#!/usr/bin/env python3
"""
0. Simple helper function
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range that takes two integer arguments
    page and page_size.
    The function should return a tuple of size
    two containing a start index and an end index
    """
    result = ()
    # Calculate the start index
    # Check if the start page = 1
    if page == 1:
        startIndex = page - 1
    if page > 1:
        startIndex = page_size * (page - 1)

    # Calculating the end index
    endIndex = page * page_size
    # endIndex = preEndIndex - 1

    # Push the result in the tuple
    lst = list(result)
    lst.append(startIndex)
    lst.append(endIndex)
    tpl = tuple(lst)

    return tpl
