#!/usr/bin/env python3
"""
This module returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find and return a list of documents in the given collection.

    :param mongo_collection: The MongoDB collection to query.
    :param topic: The topic to search for in the documents.
    :return: A list of documents that contain the specified topic.
    """
    result = mongo_collection.find(topic)
    return list(result)
