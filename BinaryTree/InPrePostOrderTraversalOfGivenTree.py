"""
Implementation of inOrder, preOrder and postOrder traversals of a tree
The traversals are implemented recursively
"""

# Importing the already created code for tree creation
# This lets us focus on the specific task in this file
# Check file with the module name in the same folder
import BinaryTreeCreation as BTC

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

    # Calling main function of the module, that creates the tree for us.
    root = BTC.BinaryTree()
    
    # Function to print Tree in inOrder traversal recursively
    print("\nInOrder Traversal:")
    inOrderRecursive(root)

    # Function to print Tree in preOrder traversal recursively
    print("\nPreOrder Traversal:")
    preOrderRecursive(root)
    
    # Function to print Tree in postOrder traversal recursively
    print("\nPostOrder Traversal:")
    postOrderRecursive(root)
