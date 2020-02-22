---
title: "Advancing through an array"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Advancing through an array" >}}
"""
Advancing through an array.
if A = <3,3,7,0,2,0,1),we iteratively compute the furthest we can advance to as 0,3,4,4,4,6,6,7, which reaches the last index, 6. lf A = (3,2,0,0,2,0,7>, we iteratively update the furthest we can advance to as 0,3,3,3,3, after which we cannot advance, so it is not possible to reach the last index.
"""

def iterateArray(arr):
    furthest_reach_so_far, last_index = 0, len(arr) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far <= last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, arr[i] + i)
        print(furthest_reach_so_far)
        i += 1
    return furthest_reach_so_far >= last_index 

arr = [3,3,1,0,2,0,1]
print(iterateArray(arr))

{{< /codecaption >}}
