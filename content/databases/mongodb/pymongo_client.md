---
title: "Pymongo_client"
date: 2019-12-12T01:41:04+05:30
 
weight: 999
---

{{% children depth="3" sort="weight" %}}

#### mongo connection in python with pymongo

    from pymongo import MongoClient
    
    client=MongoClient('mongodb://<username>:<password>@<ip>:<port>/<database>?authSource=<database>')
    
    db=client['db_name']
    
    db.collection_names()
