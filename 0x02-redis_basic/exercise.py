#!/usr/bin/env python3
'''this module define a a class cache'''
import redis
from typing import Union, Optional, Callable
import uuid


class Cache():
    '''a cache class defined that defines a store of data
    in redis cacche
    '''
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        '''this method generates a random key and store it redis
        Args:
            data: the data to be stored in redis

        Return:
            str: the generated random key
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            int, str, float, bytes]:
        """
            Retrieve a value from the cache.

            Parameters:
              - key (str): The key to retrieve from the cache.
              - fn (Optional[Callable]): callable will be used to convert
              the data back to the desired format
            Returns:
              - The value associated with the key, or the result
              of calling the provided function.
        """
        value = self._redis.get(key)
        if value and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''covert byte to string'''
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        '''convert the bytes to int'''
        return self.get(key, int)
