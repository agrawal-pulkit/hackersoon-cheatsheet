---
title: "BST"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Binary Search Tree" >}}
"""
Implementation of Binary Search Tree
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftNode:
                self.insertNode(data, node.leftNode)
            else:
                node.leftNode = Node(data)
        else:
            if node.rightNode:
                self.insertNode(data, node.rightNode)
            else:
                node.rightNode = Node(data)

    def remove(self, data):
        if self.root:
            self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftNode = self.removeNode(data, node.leftNode)
        elif data > node.data:
            node.rightNode = self.removeNode(data, node.rightNode)
        else:
            if not node.leftNode and not node.rightNode:
                print("removing a leaf node.")
                del node
                return None

            elif not node.leftNode:
                print("removing a node with single right child.")
                tempNode = node.rightNode
                del node
                return tempNode
            elif not node.rightNode:
                print("removing a node with single left child.")
                tempNode = node.leftNode
                del node
                return tempNode

            print("removing a node with two children.")
            predeccorNode = self.getPredeccorNode(node.leftNode)
            node.data = predeccorNode.data
            node.leftNode = self.removeNode(predeccorNode.data, node.leftNode)

        return node

    def getPredeccorNode(self, node):
        if node.rightNode:
            return self.getPredeccorNode(node.rightNode)

        return node

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
        else:
            return "empty tree"

    def getMin(self, node):
        if node.leftNode:
            return self.getMin(node.leftNode)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)
        else:
            return "empty tree"

    def getMax(self, node):
        if node.rightNode:
            return self.getMax(node.rightNode)
        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftNode:
            self.traverseInOrder(node.leftNode)

        print(node.data)

        if node.rightNode:
            self.traverseInOrder(node.rightNode)


bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)

bst.traverse()

bst.remove(6)

bst.traverse()
{{< /codecaption >}}