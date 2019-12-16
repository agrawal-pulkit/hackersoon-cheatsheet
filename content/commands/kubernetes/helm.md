---
title: "Helm"
date: 2019-12-12T22:57:37+05:30
 
weight: 999
---

get helm charts

    helm ls --all

    #get specific helm chart
    helm ls --all <name>

how to install a helm chart

    helm install --name <name> <path-tohelm-chart> --namespace <namespace>

    #use a specific values file
    helm install --name <name> <path-tohelm-chart> --namespace <namespace> -f <path-to-yaml-file>

    #more updated
    helm install  --name <name> <path-tohelm-chart> --namespace <namespace> --wait --timeout 1200 --set 'image.tag=latest' -f  <path-to-yaml-file>

how to install a helm chart

    helm upgrade <name> <path-tohelm-chart> --namespace <namespace>


delete a helm chart

    helm del --purge <name>

