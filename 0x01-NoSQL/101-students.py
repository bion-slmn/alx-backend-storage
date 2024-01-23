#!/usr/bin/env python3
'''
script to define Python function that returns all students 
sorted by average score
'''
from pymongo import MongoClient


def top_students(mongo_collection):
    '''mongo_collection : the pymongo collection object'''
    pipeline = [
                {'$project': {
                    '_id': 1,
                    'name': 1,
                    'averageScore': {
                        '$avg': {
                            '$avg': '$topics.score',
                            },
                        },
                    'topics': 1,
                    },
            },
                {
                    '$sort': {'averageScore': -1},
                },
                ]
    return mongo_collection.aggregate(pipeline)
