from typing import List
from queue import Queue
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if not nodes or nodes[0] is None:
            return None
        root = TreeNode(nodes[0])
        q = deque([root])
        i = 1
        while i < len(nodes):
            curr = q.popleft()
            if i < len(nodes) and nodes[i] is not None:
                curr.left = TreeNode(nodes[i])
                curr.left.parent = curr
                q.append(curr.left)
            i += 1
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i])
                curr.right.parent = curr
                q.append(curr.right)
            i += 1
        return root
    def find(self, root, value):
        if not root:
            return None
        q = deque([root])
        while q:
            currentNode = q.popleft()
            if currentNode.data == value:
                return currentNode
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        return None

def lowest_common_ancestor(p, q):
    # initialize two pinters one on each of the given node
    ptr1, ptr2 = p, q

    # Move both pointers to their respective parent nodes:
    # Continue this process until these two pointers meet.
    while (ptr1 != ptr2):
        # If a pointer reaches the root, reset it to the starting position of the other node.
        if (ptr1.parent == None):
            ptr1 = q
        else:
            ptr1 = ptr1.parent
  
        if (ptr2.parent == None):
            ptr2 = p
        else: 
            ptr2 = ptr2.parent
  
    # Return the node at which they meet as this is LCA of the given nodes.
    return ptr1