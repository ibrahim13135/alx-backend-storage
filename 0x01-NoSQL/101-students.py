#!/usr/bin/env python3

from pymongo import MongoClient
from bson.objectid import ObjectId  # Import ObjectId for converting ObjectId to string

def top_students(mongo_collection):
    pipeline = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": { "$first": "$name" },
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        },
        {
            "$project": {
                "_id": { "$toString": "$_id" },
                "formattedOutput": {
                    "$concat": [
                        "[",
                        { "$toString": "$_id" },
                        "] ",
                        "$name",
                        " => ",
                        { "$toString": { "$round": ["$averageScore", 2] } }
                    ]
                }
            }
        }
    ]
    
    cursor = mongo_collection.aggregate(pipeline)
    formatted_results = [document['formattedOutput'] for document in cursor]
    
    return formatted_results
