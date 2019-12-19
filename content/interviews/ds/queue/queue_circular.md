---
title: "Circular Queue"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Circular Queue" >}}
class Empty(Exception):
    pass

class CircularQueue:

    class _Node:

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def first(self):
        if self.isEmpty():
            raise Empty("queue is empty.")
        return self._tail._next._element

    def enqueue(self, value):
        node = self._Node(value, None)
        if self.isEmpty():
            node._next = node
        else:
            node._next = self._tail._next
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Empty("queue is empty.")
        ans = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail = self.ans._next
        self._size -= 1
        return ans._element

    def rotate(self):
        if self._size > 0:
            self._tail._next = self._tail
{{< /codecaption >}}