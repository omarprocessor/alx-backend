#!/usr/bin/env python3
"""
This module has  function named
index_range that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """This function returns a tuple of size two containing
    a start index and an end index corresponding to the range
    of indexes to return in a list for those
    particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)
