---
title: "Delete Duplicate from Array"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Delete Duplicate from Array" >}}

"""
Delete Duplicate from a sorted array.
And return number of duplicate entries after deletion.
This problem is concemed with deleting repeated elements from a sorted array. For example, for the array <2,3,5,5,7,1.1.,L1.,77,73>, then after deletion, the array is (2,3,5,7,77,73,0,0,0). After deleting repeated elements, there are 6 valid entries. There are no requirements as to the values stored beyond the last valid element.

"""
def delete_duplicate(arr):
    if len(arr) == 0:
        return
    write_index = 1
    for i in range(len(arr)): 
        if arr[write_index-1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1
    return arr[:write_index]

arr = [2,3,5,5,7,11,11,11,13]
result = delete_duplicate(arr)
print("result: ", result)

{{< /codecaption >}}
