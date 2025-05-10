#!/usr/bin/env python3
"""
This module has  function named
index_range that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    return ((page - 1) * page_size, page * page_size)
