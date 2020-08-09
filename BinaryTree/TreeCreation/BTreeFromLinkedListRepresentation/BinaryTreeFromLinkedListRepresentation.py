"""
Implementation of creating binary tree from its

given linked list representation

The code for linked list is stored in different file

and will be imported as a module in this file
"""

# Importing the LinkedList module
from LinkedList import *

# Class to denote the tree nodes
class Node:

    # Contains data and child nodes
    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None

# Function to print inOrder traversal of the tree, when created
def printTree(root):

    if root:

        printTree(root.left)

        print(root.data, end = " ")

        printTree(root.right)

# Function to build the tree from linked list
# Function uses queue to access the required node at any time
def buildTree(head):

    # Return if linked list is empty
    if not head:

        return None

    # The first node in list will always be the root
    root = Node(head.data)

    # Move to the next list node
    head = head.next

    # Initialize the queue and push current node
    que = [root]

    # Iterate till the list lasts
    while head:

        # Pop out the first in node from queue
        node = que.pop(0)

        # Insert the new node into it's left child
        node.left = Node(head.data)

        # Append it as the last in node in queue
        que.append(node.left)

        # Move the head pointer of the list
        head = head.next

        # If the list still exist
        if head:

            # Insert the next node in the poped node's right child
            node.right = Node(head.data)

            # Append it into the queue
            que.append(node.right)

            # Move the pointer to next node
            head = head.next

    # Return the root of the created tree
    return root

# The driver code
if __name__ == "__main__":

    # Create the linked list by giving necessary inputs
    head = createList()

    # Print the list
    printList(head)

    # Call the function to build the tree and return its root
    root = buildTree(head)

    # Print the inOrder traversal of the tree
    printTree(root)
