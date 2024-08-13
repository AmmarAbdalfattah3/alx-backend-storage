#!/usr/bin/env python3
"""
This module changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    result = mongo_collection.update_many(name, topics)
    return result
