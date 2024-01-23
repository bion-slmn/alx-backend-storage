#!/usr/bin/env python3
''' script to update the topics based on name in mongodb'''


def update_topics(mongo_collection, name, topics):
    '''
    parameters-
    mongo_collection: pymongo collection object
    name (string): school name to update
    topics (list of strings): list of topics approached in the school
    '''
    query = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update_one(query, newvalues)
