---
title: "DFS"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Deapth First Search" >}}
"""
initiaze a tree node
"""
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class DFS:

    def dfsByRecursion(self, startNode):

        startNode.visited = True

        print(startNode.name)

        for n in startNode.adjacencyList:
            n.visited = True
            self.dfsByRecursion(n)

    def dfsByStack(self, startNode):

        stack = []
        startNode.visited = True
        stack.append(startNode)

        while stack:
            actualNode = stack.pop()
            print(actualNode.name)

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    stack.append(n)

# sample input

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')


node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node3.adjacencyList.append(node5)

dfs = DFS()
dfs.dfsByStack(node1)

dfs.dfsByRecursion(node1)

{{< /codecaption >}}
