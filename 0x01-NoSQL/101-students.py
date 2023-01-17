#!/usr/bin/env python3
"""
returns all student sorted by average score
"""


def top_students(mongo_collection):
    """
    returns all student sorted by average score
    """

    return mongo_collection.aggregate(
        [{"$unwind": "$topics"}, {"$group": {
            "_id": "$_id", "averageScore": {
                "$avg": "$topics.score"}, "name": {
                "$first": "$name"}}}])
