---
title: "Computing Alteration of an Array"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Computing Alteration of an Array" >}}

def rearrange(arr):
    for i in range(len(arr)):
        arr[i:i+2] = sorted(arr[i:i+2], reverse=i%2)
    return  arr

arr = [2, 3, 4, 5, 6, 2, 3, 4]
result = rearrange(arr)
print("result: ", result)

{{< /codecaption >}}