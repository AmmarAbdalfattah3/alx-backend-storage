#!/usr/bin/env python3
"""
This module changes all topics of a school document based on the name
"""


from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Update all topics of a school document based on the name.

    Args:
        mongo_collection (Collection): The pymongo collection object.
        name (str): The name of the school document to update.
        topics (List[str]): The list of topics to set in the document.

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
