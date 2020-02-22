---
title: "Computing Alteration of an Array"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Computing Alteration of an Array" >}}

"""
Write a program that takes an array A of n numbers, and rearranges A's elements to get a new array BhavingthepropertythatB[0] < B[1] >Bl2) < B[3] >8141< B[5] >....

you may notice that the desired ordering is very local, and realize that it is not necessary to find the median. Iterating through the array and swapping A[i] and AU + 1l when i is even and
Alil > Ali + 1l or I is odd and A[4 < Ali + 1] achieves the desired configuration. In code:
"""
def rearrange(arr):
    for i in range(len(arr)):
        arr[i:i+2] = sorted(arr[i:i+2], reverse=i%2)
    return  arr

arr = [2, 3, 4, 5, 6, 2, 3, 4]
result = rearrange(arr)
print("result: ", result)

{{< /codecaption >}}