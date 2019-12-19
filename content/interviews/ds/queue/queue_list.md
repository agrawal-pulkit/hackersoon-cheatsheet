---
title: "Queue List"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Queue List" >}}
class Empty(Exception):
    pass

class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return  self._size == 0

    def first(self):
        if self.isempty():
            raise Empty("queue is empty.")
        return self._data[self._front]

    def enqueue(self, value):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = value
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise Empty("queue is empty.")
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return ans

    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data.append(old[walk])
            walk = (1+walk)%len(old)
        self._front = 0

{{< /codecaption >}}