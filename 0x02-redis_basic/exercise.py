#!/usr/bin/env python3
"""this module create a Cache class"""
import redis
import uuid
from typing import Union


class Cache:
    """This class is that deines a way to store data
    in a Redis cache
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """it stores a key in database.
        Args:
            data (Union[str, bytes, int, float]): An argument
        Returns:
            str: the generated random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
