---
title: "Duch National Flag Problem"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---


{{< codecaption lang="python" title="Duch National Flag Problem" >}}

"""
Rearragement of numbers based on pivot number.
suppose A = (0,1.,2,0,2,1,L), and the pivot index is 3. 
Then A[3] = 0, so <0,0,7,2,2,L,1) is a valid partitioning. 
For the same array, if the pivot index is 2, 
then Al2l = 2, the arrays <0,7,0,1,1,2,2> 
as well as (0,0, 7,1,,'1,,2,2> are valid partitionings.

"""

def rearragement(arr, pivot):
    s, e, l = 0, 0, len(arr)

    while e < l:
        if arr[e] < pivot:
            arr[e], arr[s] = arr[s], arr[e]
            s += 1
            e += 1
        elif arr[e] == pivot:
            e += 1
        else:
            l -= 1
            arr[l], arr[e] = arr[e], arr[l]
    return arr
    

arr = [2, 4, 0, 1, 2, 0, 2, 1, -1]
pivot = 1
print("input: ", arr, pivot)
result = rearragement(arr, pivot)
print("output: ", result)

{{< /codecaption >}}
