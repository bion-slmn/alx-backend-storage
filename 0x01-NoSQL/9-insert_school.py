#!/usr/bin/env python3
'''this module defines a fucntion that inserts a new document
into a collection'''


def insert_school(mongo_collection, **kwargs):
    '''inserts a new document into a collection and return its id'''
    x = mongo_collection.insert_one({**kwargs})
    return x.inserted_id
