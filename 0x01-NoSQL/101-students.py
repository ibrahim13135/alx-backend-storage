#!/usr/bin/env python3

from pymongo import MongoClient

def top_students(mongo_collection):
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$name",
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]
    
    return list(mongo_collection.aggregate(pipeline))
