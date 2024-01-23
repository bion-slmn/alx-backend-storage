#!/usr/bin/env python3
'''a script that provides stats about nginx logs stored in mongodb'''
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    document_no = nginx_collection.count_documents({})
    print('{} logs'.format(document_no))
    print('Methods:')
    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        count = nginx_collection.count_documents({'method': method})
        print('   method {}: {}'.format(method, count))

    status_count = nginx_collection.count_documents({'path': '/status'})
    print('{} status check'.format(status_count))
