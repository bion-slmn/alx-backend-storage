#!/usr/bin/env python3
"""this module create a Cache class"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def replay(method: Callable) -> None:
    '''function to display the history of calls of another
    function'''
    key = method.__qualname__
    redis_client = redis.Redis(decode_responses=True)

    inputs = redis_client.lrange("{}:inputs".format(key), 0, -1)
    outputs = redis_client.lrange("{}:outputs".format(key), 0, -1)

    print('{} was called {} times'.format(key, len(inputs)))
    for arg, result in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(key, arg, result))


def call_history(method: Callable) -> Callable:
    '''decorator function to store the history of tiputs  and outputs
    of a function'''
    key = method.__qualname__

    @wraps(method)
    def inner(self, *args, **kwargs):
        '''inner function of decorator function'''
        inputkey = key + ":inputs"
        outputkey = key + ":outputs"
        self._redis.rpush(inputkey, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputkey, result)
        return result

    return inner


def count_calls(method: Callable) -> Callable:
    """
    dcorator that counts number of time sthe method is called
    a Callable
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        function to  increments the count for that key every time
        method is called
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """This class is that deines a way to store data
    in a Redis cache
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
