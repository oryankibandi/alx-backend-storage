#!/usr/bin/env python3
"""Gets html from a url
"""


import requests
import redis
import typing


def increment(func: typing.Callable) -> typing.Callable:
    """Increments number of calls"""
    def wrapper(url: str) -> typing.Callable:
        """Increments number of calls"""
        r = redis.Redis()
        existing_count = r.get('count:{}'.format(url))
        if existing_count is None:
            r.setex('count:{}'.format(url), 10, 1)
        else:
            r.setex('count:{}'.format(url), 10, int(existing_count) + 1)
        return func()

    return wrapper


@increment
def get_page(url: str) -> str:
    """retrieves a web page"""
    r = requests.get(url)

    return r.text
