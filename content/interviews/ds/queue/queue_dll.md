---
title: "Queue dll"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Queue dll" >}}
class Empty(Exception):
    pass

class _DoublyLinkedBase:

    class _Node:

        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._tailer = self._Node(None, None, None)
        self._header._next = self._tailer
        self._tailer._next = self._header
        self._size = 0

    def __len__(self):
        self._size

    def isEmpty(self):
        return self._size == 0

    def _insert_between(self, value, predecessor, successor):
        node = self._Node(value, predecessor, successor)
        predecessor._next = node
        successor._prev = node
        self._size += 1
        return node

    def _delete_between(self, node):
        ans = node._element
        node._next._prev = node._prev
        node._prev._next = node._next
        self._size -= 1
        node._element = node._prev = node._next = None
        return ans



class LinkedDeque(_DoublyLinkedBase):

    def first(self):
        if self.isEmpty():
            raise Empty("queue is empty.")
        return self._header._next._element

    def last(self):
        if self.isEmpty():
            raise Empty("queue is empty.")
        return  self._tailer._prev._element

    def insert_first(self, value):
        self._insert_between(value, self._header, self._header._next)

    def insert_last(self, value):
        self._insert_between(value, self._tailer._prev, self._tailer)

    def delete_first(self):
        if self.isEmpty():
            raise Empty("queue is empty.")
        self._delete_between(self._header._next)

    def delete_last(self):
        if self.isEmpty():
            raise Empty("queue is empty.")
        self._delete_between(self._tailer._prev)

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
{{< /codecaption >}}