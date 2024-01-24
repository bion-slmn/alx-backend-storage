#!/usr/bin/env python3
'''this module define a a class cache'''
import redis
from typing import Union
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
