#!/usr/bin/env python3
"""BasicCache module that inherits from BaseCaching
and implements a simple caching system without limit."""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines a caching system with no limit."""

    def put(self, key, item):
        """Add an item in the cache using the provided key.

        If either the key or item is None, do nothing.

        Args:
            key: The key under which to store the item.
            item: The item to be stored in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
