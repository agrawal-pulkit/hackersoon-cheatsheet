---
title: "Heapsort"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="heapsort" >}}
"""
This method is used for heapify the array. 
every time when we remove a element from array.
"""
def heapify(arr, n, i):
    largest = i
    r = 2*i + 1
    l = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

"""
Actual impelementation of heap short algorithm.
"""
def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n , i)
    print(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

if __name__ == "__main__":
    arr = [ 12, 11, 13, 5, 6, 7]
    heapsort(arr)
    print(arr)
{{< /codecaption >}}
