#!/usr/bin/env python3
'''this module define a a class cache'''
import redis
from typing import Union
import uuid


class Cache():
    '''a cache class defined'''
    def __init__(self):
        '''intialising the class'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        '''this method generates a random key and store it redis'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable =None)
