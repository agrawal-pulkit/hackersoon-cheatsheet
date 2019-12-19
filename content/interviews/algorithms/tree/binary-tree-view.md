---
title: "Binary Tree Views"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Binary Tree Views" >}}
class Node:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def printMirrorView(self, node):

        q = []
        q.append(node)

        while q:
            node = q.pop(0)

            node.leftChild, node.rightChild = node.rightChild, node.leftChild
            if node.leftChild:
                q.append(node.leftChild)
            if node.rightChild:
                q.append(node.rightChild)


    def leftView(self, node):
        if not node:
            return

        while node is not None:
            print(node.data)
            if node.leftChild:
                node = node.leftChild
            else:
                node = node.rightChild


    def traverseInOrder(self, node):

        if not node:
            return

        self.traverseInOrder(node.leftChild)
        print(node.data)
        self.traverseInOrder(node.rightChild)

def createTree():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.leftChild = Node(2)
    bt.root.rightChild = Node(3)
    bt.root.leftChild.leftChild = Node(4)
    bt.root.leftChild.rightChild = Node(5)
    bt.root.leftChild.leftChild.leftChild = Node(6)
    return bt

if __name__ == "__main__":

    # bt = createTree()
    # bt.traverseInOrder(bt.root)
    # bt.printMirrorView(bt.root)
    # bt.traverseInOrder(bt.root)

    bt1 = createTree()
    #bt1.traverseInOrder(bt1.root)
    bt1.leftView(bt1.root)
    #bt1.traverseInOrder(bt1.root)

{{< /codecaption >}}