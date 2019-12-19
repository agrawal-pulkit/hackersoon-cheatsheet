---
title: "Mergesort"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="mergesort" >}}
"""
merge logic:
    This function merge two shorted arrays into one sorted array.
"""
def merge(arr, l, m ,r):

    n1 = m - l +1
    n2 = r - m

    L = [0]*n1
    R = [0]*n2

    for i in range(0, n1):
        L[i] = arr[l+i]

    for j in range(0, n2):
        R[j] = arr[m+1+j]

    i, j, k =(0, 0, l)

    while i<n1 and j<n2:

        if L[i]<=R[j]:
            arr[k] = L[i]
            i += 1

        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

"""
Actual impelementation of merge short algorithm.
"""
def mergesort(arr, l, r):

    if l < r:

        m = (l+r-1)//2

        mergesort(arr, l, m)
        mergesort(arr, m+1, r)
        merge(arr, l, m, r)

# sample input

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is: ", arr)
mergesort(arr, 0, n - 1)
print("\n\nSorted array is: ", arr)
{{< /codecaption >}}
