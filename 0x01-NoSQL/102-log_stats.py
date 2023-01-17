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
    status_checks = ng_coll.count_documents(
        {"path": {"$regex": 'status'}, "method": "GET"})
    popular_ips = ng_coll.aggregate([{"$group": {"_id": "$ip", "count": {
        "$sum": 1}}}, {"$sort": {"count": -1}}, {"$limit": 10}])

    print("{} logs".format(logs))
    print("Methods:")
    print("\tmethod GET: {}".format(gets))
    print("\tmethod POST: {}".format(posts))
    print("\tmethod PUT: {}".format(puts))
    print("\tmethod PATCH: {}".format(patchs))
    print("\tmethod DELETE: {}".format(deletes))
    print("{} status check".format(status_checks))

    print("IPs:")
    for ip in popular_ips:
        print("\t{}: {}".format(ip.get('_id'), ip.get('count')))
