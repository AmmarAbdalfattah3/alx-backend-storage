#!/usr/bin/env python3
"""
This module changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the name.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        name (str): The name of the school document to update.
        topics (List[str]): The list of topics to set in the document.

    Returns:
        None
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
        )
