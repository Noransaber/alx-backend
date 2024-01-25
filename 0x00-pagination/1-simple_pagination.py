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



class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
