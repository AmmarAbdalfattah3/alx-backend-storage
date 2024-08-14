#!/usr/bin/env python3
"""
This module provides some stats about Nginx logs stored in MongoDB.
"""


from pymongo import MongoClient



def log_stats():
    """
    This function provides stats about nginx logs stored in mongodb
    """
    client = MongoClient('mongodb://127.0.0.1:27017')

    db = client.logs
    nginx_collection = db.nginx

    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
