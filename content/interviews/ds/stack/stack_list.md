---
title: "Stack List"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Stack List" >}}
"""
Implementing a stack using python list.
"""

class Empty(Exception):
    pass

class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def push(self, value):
        self._data.append(value)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def is_empty(self):
        return self.__len__() == 0

def is_matched(expr):
    lefty = '[{('
    righty = ']})'
    s = ArrayStack()
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False

    return s.is_empty()
{{< /codecaption >}}