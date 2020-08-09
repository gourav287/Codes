"""
Implementation of a python program to create a binary tree
when the PreOrder and PostOrder traversals of the tree are given.

You can't create unique binary tree by preOrder and postOrder traversals
so there can be multiple answers. But full BT are uniquely created by them.

A "full BT" is a tree in which every node has either 0 or 2 children.

This code will implement the binary tree which will be correct,
but will not be unique to the given traversal if its not full
"""

# Class to create a tree node
class Node:

    def __init__(self, data):

        # Contains data and link for both child nodes
        self.data = data

        self.left = None

        self.right = None

# Function to print the inorder traversal of a tree, once created
def printInorder(start):

    # if the tree exists
    if start:

        # Traverse left subtree
        printInorder(start.left)

        # print value
        print(start.data, end = " ")

        # Traverse right subtree
        printInorder(start.right)

"""
Creation of the Tree from preOrder and postOrder traversals
"""
def createTree(preOrder, postOrder):

    # Variable to keep track of the preOrder list
    global preInd

    # If postOrder ends, means no more checking as nothing exists
    # or everything has already been worked upon
    if not postOrder:

        return None

    # Create a node for current element
    node = Node(preOrder[preInd])

    # Access the next element through global index
    preInd += 1

    # If the preOrder hasn't ended yet
    if preInd < len(preOrder):

        # Get the value of preOrder element and get it's index in postOrder
        # This element will be used to decide left and right subtree
        # of current node
        checkVal = preOrder[preInd]

        if checkVal in postOrder:

            ind = postOrder.index(preOrder[preInd])

            node.left = createTree(preOrder, postOrder[:ind + 1])

            # Skip the last node of postOrder as it's always the current node
            node.right = createTree(preOrder, postOrder[ind + 1:-1])

    # Return the node
    return node

# The driver code
if __name__ == '__main__':

    # preOrder traversal of the tree
    preOrder = list(map(int, input().split())) #[1, 2, 3, 4, 5, 6]

    # inOrder traversal of the tree
    postOrder = list(map(int, input().split())) #[3, 4, 2, 6, 5, 1]
    
    # Index to keep track of preOrder elements
    preInd = 0

    # Function to create the tree from inOrder and preOrder
    # traversal given to us
    start = createTree(preOrder, postOrder)

    # printing the inOrder traversal of the tree created
    print("InOrder traversal of the created tree:")
    printInorder(start)
