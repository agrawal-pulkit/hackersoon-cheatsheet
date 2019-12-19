---
title: "AVL"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="AVL Tree" >}}
class Node:

    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None


class AVL:

    def __init__(self):
        self.root = None

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) -self.calcHeight(node.rightChild)

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)

        if data<node.data:
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        return self.settleViolations(data, node)

    def settleViolations(self, data, node):

        balance = self.calcBalance(node)
        print("balance: ", balance)
        if balance > 1 and data < node.leftChild.data:
            print("Left Left heavy situation.")
            return self.rotateRight(node)

        if balance < -1 and data > node.rightChild.data:
            print("Right Right heavy situation.")
            return self.rotateLeft(node)

        if balance > 1 and data > node.leftChild.data:
            print("Left Right Heavy situation.")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightChild.data:
            print("Right Left Heavy situation.")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node

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

        if not node:
            return node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1

        balance = self.calcBalance(node)

        if balance > 1 and self.calcBalance(node.leftChild)>=0:
            print("Left Left heavy situation.")
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.rightChild)<=0:
            print("Right Right heavy situation.")
            return self.rotateLeft(node)

        if balance > 1 and self.calcBalance(node.leftChild)<0:
            print("Left Right Heavy situation.")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.rightChild)>0:
            print("Right Left Heavy situation.")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)

        return node


    def getPredeccorNode(self, node):
        if node.rightNode:
            return self.getPredeccorNode(node.rightNode)

        return node

    def rotateRight(self, node):

        tempLeftNode = node.leftChild
        t = tempLeftNode.rightChild

        tempLeftNode.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftNode.height = max(self.calcHeight(tempLeftNode.leftChild), self.calcHeight(tempLeftNode.rightChild)) + 1

        return tempLeftNode

    def rotateLeft(self, node):

        tempRightNode = node.rightChild
        t = tempRightNode.leftChild

        tempRightNode.leftChild = node
        node.rightChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightNode.height = max(self.calcHeight(tempRightNode.leftChild), self.calcHeight(tempRightNode.rightChild)) + 1

        return tempRightNode

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print(node.data)

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

{{< /codecaption >}}