#!/usr/bin/env python3
"""
This module contains the Cache class which provides a simple interface
to store data in Redis.
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class for storing data in Redis with random keys.
    """

    def __init__(self):
        """
        Initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve the data stored in Redis for the given key and optionally
        convert it using the provided function.

        Args:
            key (str): The key of the data to retrieve.
            fn (Callable, optional): A function to convert the data. Defaults to None.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data stored in Redis for the given key and convert it to a string.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            Optional[str]: The retrieved data as a string or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data stored in Redis for the given key and convert it to an integer.

        Args:
            key (str): The key of the data to retrieve.

        Returns:
            Optional[int]: The retrieved data as an integer or None if the key does not exist.
        """
        return self.get(key, fn=int)
