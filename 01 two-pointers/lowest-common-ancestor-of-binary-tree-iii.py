# Definition for a binary tree node
class EduTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

# from EduTreeNode import *

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