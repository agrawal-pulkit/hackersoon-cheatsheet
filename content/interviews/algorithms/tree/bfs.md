---
title: "BFS"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Breadth First Search" >}}
class Node:

    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class BFS:

    def bfs(self, startNode):

        queue = []
        startNode.visited = True
        queue.append(startNode)

        while queue:
            actualNode = queue.pop(0)
            print(actualNode.name)

            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.append(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')


node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node3.adjacencyList.append(node5)

bfs = BFS()
bfs.bfs(node1)
{{< /codecaption >}}
