#!/usr/bin/env python3
"""
Cache class with a Redis client instance.
"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        # Convert arguments to a string and store in Redis
        self._redis.rpush(inputs_key, str(args))

        # Call the original method and get the output
        output = method(self, *args, **kwargs)

        # Store the output in Redis
        self._redis.rpush(outputs_key, output)

        # Return the output
        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """Initialize the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable[[bytes], Union[str, int, float]]] = None
    ) -> Optional[Union[str, int, float]]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, int)
