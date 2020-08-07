"""
Implementation of a python program to create a binary tree
when the inOrder and PreOrder traversals of the tree are given.
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
Creation of the Tree from inOrder and preOrder traversals
"""
def createTree(inOrder, preOrder, left, right):

    # A global variable to keep track of current preOrder element
    global cur_ind

    # If no element in the desired part of list
    if left > right:

        return None

    # Create a tree node from element of preOrder traversal
    # Increase the global variable's index value
    tmp = Node(preOrder[cur_ind])

    cur_ind += 1

    # If left == right then the node is leaf
    # Else work on to create child nodes as follows
    if left != right:

        # Getting the index in inOrder
        # This tells us about left and right subtree
        # of the current node
        ind = inOrder.index(tmp.data)

        # Recursively run the code for left subtree
        tmp.left = createTree(inOrder, preOrder, left, ind - 1)

        # Recursively run the code for right subtree
        tmp.right = createTree(inOrder, preOrder, ind + 1, right)

    # Returning the node to be added to the tree
    return tmp

# The driver code
if __name__ == '__main__':

    # inOrder traversal of the tree
    inOrder = list(map(int, input().split())) #[1, 2, 3, 4, 5, 6, 7]

    # preOrder traversal of the tree
    preOrder = list(map(int, input().split())) #[4, 2, 1, 3, 6, 5, 7]

    # Index to keep track of preOrder elements
    cur_ind = 0

    # Function to create the tree from inOrder and preOrder
    # traversal given to us
    start = createTree(inOrder, preOrder, 0, len(inOrder) - 1)

    # printing the inOrder traversal of the tree created
    printInorder(start)
