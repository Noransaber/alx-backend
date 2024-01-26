#!/usr/bin/env python3
"""Task 1: Simple pagination.
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


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
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary
        """
        # calculate the start and the end of the page by index_range method
        start, end = index_range(page, page_size)
        page_len = end - start
        current_page = end - start
        total_pages = end - start + 1
        data = self.dataset()
        page_data = data[start: end]
        if not end + 1:
            return None
        next_page = end + 1
        if not start - 1:
            return None
        prev_page = start - 1
        return {'page_size': page_len, 'page': current_page, 'data': page_data, 'next_page': next_page, 'prev_page': prev_page, 'total_pages': total_pages}


# {'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
        
