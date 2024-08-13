#!/usr/bin/env python3
"""
This module inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.
        **kwargs: Arbitrary keyword arguments for the document fields.

    Returns:
        The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
