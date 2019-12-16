---
title: "Kubernetes"
date: 2019-12-12T22:57:37+05:30
 
weight: 999
---

{{% children depth="3" sort="weight" %}}


    alias k=kubectl

get objects

    k get pods -n <namespace>

    k get deployments -n <namespace>

    k get services -n <namespace>

    # example
    k get <object> -n <namespace>

    # get in all namespaces

    k get <object> --all-namespaces

edit kubernetes objects

    k edit <object> <name> -n <namespace>

describe kubernetes objects
    
    k describe <object> <name> -n <namespace>

delete object

    k delete <object> -n <namespace>

enter inside a container

    k exec -it <pod_name> -n <namespace> /bin/sh

scale a deployment

    kubectl scale deployment <deployment_name> --replicas=<number of replica>

    # scale all deployment with one command
    kubectl get deploy -n <namespace> -o name | xargs -I % kubectl scale % --replicas=1 -n services


get all pods which is running on a particular node:

    kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=<node-name>

Secrets

    k get secrets -n  <namespace> 

    # get a particular secret
    k get secret -n <namespace> -o yaml

    # copy secret value and decode it
    echo "value" | base64 -D
