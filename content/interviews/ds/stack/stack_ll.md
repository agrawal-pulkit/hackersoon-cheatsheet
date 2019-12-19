---
title: "Stack LL"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Stack LL" >}}
class Empty(Exception):
    pass

class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, value):
        self._head = self._Node(value, self._head)
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise Empty("stack is empty.")
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        return ans

    def top(self):
        if self._size == 0:
            raise Empty("stack is empty.")
        return self._head._element
{{< /codecaption >}}