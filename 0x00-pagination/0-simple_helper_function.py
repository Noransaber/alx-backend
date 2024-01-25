#!/usr/bin/env python3
"""
0. Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
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
    
    
res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)
