#!/usr/bin/env python3
'''This defines a function that lists all the documents
in a collection '''


def list_all(mongo_collection):
    '''list all the documents in the given colllection
    return a list with the documents or empty list if no doc
    '''
    all_doc = []
    all_doc = mongo_collection.find()
    return all_doc
