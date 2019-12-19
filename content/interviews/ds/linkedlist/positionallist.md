---
title: "Positional List"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Positional List" >}}
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


class PositionalList(_DoublyLinkedBase):

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)


    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Postion type.")
        if p._container is not self:
            raise ValueError("P does not belongs to this container.")
        if p._node._next is None:
            raise ValueError("p is no longer valid.")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._tailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._tailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, value, predecessor, successor):
        node = super()._insert_between(value, predecessor, successor)
        return self._make_position(node)

    def add_first(self, value):
        return self._insert_between(value, self._header, self._header._next)

    def add_last(self, value):
        return self._insert_between(value, self._tailer._prev, self._tailer)

    def add_befor(self, value, p):
        original = self._validate(p)
        return self._insert_between(value, original._prev, original)

    def add_after(self, value, p):
        original = self._validate(p)
        return self._insert_between(value, original, original._next)

    def _delete_between(self, p):
        original = self._validate(p)
        return self._delete_between(original)

    def replace(self, p , value):
        original = self._validate(p)
        ans = original._element
        original._element = value
        return ans
{{< /codecaption >}}