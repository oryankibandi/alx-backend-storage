#!/usr/bin/env python3

import redis
import uuid
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    """increments counter"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(str(method.__qualname__))
        return method(*args, **kwargs)

    return wrapper


def call_history(method: typing.Callable) -> typing.Callable:
    """stores history"""
    input_list = "{}:inputs".format(method.__qualname__)
    output_list = "{}:outputs".format(method.__qualname__)

    def wrapper(self, *args, **kwargs):
        """stores argument history"""
        for arg in args:
            self._redis.rpush(input_list, str(arg))

        output = method(*args, **kwargs)
        self._redis.rpush(output_list, output)

        return output

    return wrapper


@count_calls
@call_history
class Cache:
    """Cache class
    """

    def __init__(self):
        """Initializes the class properties"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """stores data in Redis"""
        uid = uuid.uuid4()
        self._redis.set(str(uid), data)
        return str(uid)

    def get(self, key: str, fn: typing.Callable):
        """converts the data back to the desired format"""
        value = self._redis.get(key)
        if fn is not None:
            return fn(value)
        else:
            return value
