#!/usr/bin/env python3
import requests
import redis
from functools import wraps
from hashlib import sha256

# Initialize Redis client
redis_client = redis.Redis()

def cache_and_count(func):
    @wraps(func)
    def wrapper(url: str, *args, **kwargs):
        # Generate a unique key for caching based on the URL
        cache_key = f"cache:{sha256(url.encode()).hexdigest()}"
        count_key = f"count:{url}"

        # Check if the URL content is already cached
        cached_content = redis_client.get(cache_key)
        if cached_content:
            # Increment the access count
            redis_client.incr(count_key)
            return cached_content.decode('utf-8')

        # Fetch the URL content if not cached
        html_content = func(url, *args, **kwargs)

        # Cache the result with an expiration time of 10 seconds
        redis_client.setex(cache_key, 10, html_content)
        
        # Increment the access count
        redis_client.incr(count_key)
        
        return html_content
    return wrapper

@cache_and_count
def get_page(url: str) -> str:
    """
    Fetch the HTML content of a URL.
    """
    response = requests.get(url)
    return response.text

