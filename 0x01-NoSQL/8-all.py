#!/usr/bin/env python3
"""
This module lists all documents in a collection
"""


from typing import List, Dict


def list_all(mongo_collection) -> List[Dict]:
    """
    Lists all documents in a collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
        List[Dict]: A list of documents in the collection. Returns an empty list if no documents.
    """
    return list(mongo_collection.find())
