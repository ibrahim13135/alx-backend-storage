#!/usr/bin/env python3
"""
Log stats - new version
Provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


def log_stats():
    """
    Prints the following statistics about Nginx logs in MongoDB:
    - Total number of logs
    - Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of status check logs (path: /status)
    - Top 10 most frequent IPs
    """
    # Connect to the MongoDB server
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Count the total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count the occurrences of each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count the number of status checks
    status_check_count = collection.count_documents({"path": "/status"})
    print(f"{status_check_count} status check")

    # Find the top 10 most present IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(collection.aggregate(pipeline))

    # Print the top 10 IPs
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
