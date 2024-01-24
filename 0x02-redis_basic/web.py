#!/usr/bin/env python3
''' this module implements function track how many times a url is called'''

import requests
import redis
from typing import Callable


def counter_fun(func: Callable) -> Callable:
    '''decorator to track how many times a url is called
    and cache but the cache expires in 10sec'''
    redis_client = redis.Redis(decode_responses=True)

    def inner(url):

        cached_html = redis_client.get(url)
        if cached_html:
            return cached_html

        key = 'count:' + url
        redis_client.incr(key)

        result = func(url)
        redis_client.set(url, result, ex=10)

        return result
    return inner


@counter_fun
def get_page(url: str) -> str:
    '''this function get a page and return the html of tha page'''
    html = requests.get(url).text
    return html
