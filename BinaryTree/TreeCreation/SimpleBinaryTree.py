"""
Implement simple binary tree. It can have leaf nodes at
different levels and is not a complete binary tree
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

"""Iteratively building the Tree with the help of stack"""
def buildTree(vals):

    # Initialising the index for values to be added to tree
    i = 0

    # If the vals array actually exists
    if vals:

        # Initializing the root node
        root = Node(vals[int(i)])
        i += 1

        # Pushing the root node into the queue
        queue = [root]

        # While queue is not empty and the value list isn't traversed till end
        while queue and i < len(vals):

            # Pop the node in front element of queue
            curr = queue.pop(0)

            # If it is empty, do nothing
            if vals[i] != 'N':

                # Append to the left of current node and push into the queue
                curr.left = Node(vals[int(i)])

                queue.append(curr.left)
            
            i += 1

            # Do the same for the right child of current node
            if i < len(vals) and vals[i] != 'N':

                curr.right = Node(vals[int(i)])

                queue.append(curr.right)

            i += 1

    # Return the tree created
    return root


# The main function
def BinaryTree():

    # Input total number of nodes in the tree
    n = int(input())

    # Inputing the values of Binary Tree nodes
    vals = list(map(str, input().split()))

    # Initialising a queue
    queue = []

    # Calling the function to build the tree
    root = buildTree(vals)

    # Return the root node of the tree
    return root

# The driver code
if __name__ == "__main__":

    # Calling the BinaryTree function to input necessary parameters
    # And create the tree
    root = BinaryTree()

    # Printing the tree
    printTree(root)
