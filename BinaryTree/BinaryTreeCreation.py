"""
This file contains creation of a simple Binary Tree
"""

# Class representing single node of the tree
class Node:

    # Constructor initializing data and child links
    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None

# Printing the inorder traversal of the tree
def printTree(root):

    # If the tree exist
    if root:

        # Go to the left most end
        printTree(root.left)

        # print the value
        print(root.data, end = " ")

        # Go to the right part
        printTree(root.right)

"""
This function is used to build a binary tree when
list of node values are given
"""
def buildTree(root, val):

    # If the tree doesn't exist yet, just create it
    if not root:

        root = Node(val)

    # Otherwise use a queue to achieve level wise traversal
    # And update the list
    else:

        # Queue creation
        q = []
        
        q.append(root)

        # Looping till last element
        while len(q):

            # creating temporary pointer to current node
            tmp = q[0]

            # Dequeue one element that is being accessed currently
            q.pop(0)

            # If the current node has no left child, add one and stop
            if not tmp.left:

                tmp.left = Node(val)

                break

            # If left child exist, just append it to the queue
            else:

                q.append(tmp.left)

            # If the current node has no right child, add one and stop
            if not tmp.right:

                tmp.right = Node(val)

                break

            # If right child exist, just append it to the queue
            else:

                q.append(tmp.right)

    # Returning the root node of the tree
    return root


# The driver code
if __name__ == '__main__':

    # Input length of list
    n = int(input())

    # Inputing the values of Binary Tree nodes
    vals = list(map(int, input().split()))

    # Creating root for the first time
    root = None

    # Iterating through the values and updating the tree
    for v in vals:

        root = buildTree(root, v)

    # Print the inorder traversal of the tree
    printTree(root)
