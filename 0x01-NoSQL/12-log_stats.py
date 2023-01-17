#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""

if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient()
    db = client.logs
    ng_coll = db.nginx

    logs = ng_coll.count_documents({})
    gets = ng_coll.count_documents({"method": "GET"})
    posts = ng_coll.count_documents({"method": "POST"})
    puts = ng_coll.count_documents({"method": "PUT"})
    patchs = ng_coll.count_documents({"method": "PATCH"})
    deletes = ng_coll.count_documents({"method": "DELETE"})
    status_checks = ng_coll.count_documents({"path": {"$regex": 'status'}})

    print("{} logs".format(logs))
    print("Methods:")
    print("    method GET: {}".format(gets))
    print("    method POST: {}".format(posts))
    print("    method PUT: {}".format(puts))
    print("    method PATCH: {}".format(patchs))
    print("    method DELETE: {}".format(deletes))
    print("{} status check".format(status_checks))
