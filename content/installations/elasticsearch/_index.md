---
title: "ElasticSearch"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{% children depth="3" sort="weight" %}}

## Elasticsearch installation in Ubuntu:


    apt-get update
    apt-get install python-minimal
    apt-get install openjdk-8-jdk
    wget https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/2.4.0/elasticsearch-2.4.0.deb
    dpkg -i elasticsearch-2.4.0.deb
    
    cd /etc/elasticsearch
    vim elasticsearch.yml
    
    update network.host with private ip of the server
    
    service elasticsearch start
    service elasticsearch status
    
    curl ip:9200/