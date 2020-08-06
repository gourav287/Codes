"""
Implementation of inOrder, preOrder and postOrder traversals of a tree
The traversals are implemented recursively
"""

# Importing the already created code for tree creation
# This lets us focus on the specific task in this file
# Check file with the module name in the same folder
from BinaryTreeCreation import *

# Implementation of inOrder traversal
def inOrderRecursive(root):

    # If the node exists
    if root:

        # Go left
        inOrderRecursive(root.left)

        # Print node value
        print(root.data, end = " ")

        # Go right
        inOrderRecursive(root.right)

# Implementation of preOrder traversal
def preOrderRecursive(root):

    # If the node exists
    if root:

        # print node value
        print(root.data, end = " ")

        # Go left
        inOrderRecursive(root.left)

        # Go right
        inOrderRecursive(root.right)

# Implementation of postOrder traversal
def postOrderRecursive(root):

    # If the node exists
    if root:

        # Go left
        inOrderRecursive(root.left)

        # Go right
        inOrderRecursive(root.right)

        # Print node value
        print(root.data, end = " ")


# The driver code
if __name__ == '__main__':

    # Input total no of nodes of the tree
    n = int(input())

    # Input values of the nodes
    vals = list(map(int, input().split()))

    # Creating root node
    root = None

    # Iterating through each node
    for v in vals:

        # This predefined function (from module) builds the tree
        # It takes values of list vals as min level order traversal of the tree
        root = buildTree(root, v)

    # Function to print Tree in inOrder traversal recursively
    print("\nInOrder Traversal:")
    inOrderRecursive(root)

    # Function to print Tree in preOrder traversal recursively
    print("\nPreOrder Traversal:")
    preOrderRecursive(root)
    
    # Function to print Tree in postOrder traversal recursively
    print("\nPostOrder Traversal:")
    postOrderRecursive(root)
