---
title: "Queue LL"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Queue LL" >}}
class Empty(Exception):
    pass

class LinkedQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def first(self):
        if self.isempty():
            raise Empty("queue is empty.")
        return self._head._element

    def enqueue(self, value):
        node = self._Node(value, self._head)
        if self.isempty():
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if self.isempty():
            raise Empty("queue is empty.")
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._tail = None
        return ans
{{< /codecaption >}}