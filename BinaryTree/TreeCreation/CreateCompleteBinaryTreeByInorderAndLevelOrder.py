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

# Function to print the preorder traversal of a tree, once created
def printPreOrder(root):

    # If the tree exists
    if root:

        # Print the data
        print(root.data, end = " ")

        # Traverse left subtree
        printPreOrder(root.left)

        # Traverse right subtree
        printPreOrder(root.right)

"""
Creation of the Tree from inOrder and level order traversals
"""
def buildTree(inOrder, levOrder):

    # If inorder is there (traversal remains in subtree)
    if inOrder:

        # Traversing through the level order
        for i in range(len(levOrder)):

            # If we find required node to add just create a node
            # and store its value then break the further iteration
            if levOrder[i] in inOrder:

                node = Node(levOrder[i])

                inIndex = inOrder.index(levOrder[i])

                break

        # Do the same for left and right childs of the node
        node.left = buildTree(inOrder[:inIndex], levOrder)

        node.right = buildTree(inOrder[inIndex+1:len(inOrder)], levOrder)

        # Return the node to it's predecessor
        return node

# The main function
def main():

    # Input the inorder traversal of the tree
    inOrder = list(map(int, input().split()))

    # Input the level order traversal of the tree
    levOrder = list(map(int, input().split()))

    # Call the function to build the tree
    root = buildTree(inOrder, levOrder)

    # Returning the root of the created Binary Tree
    return root

# The driver code
if __name__ == '__main__':

    # Calling the main function to create and return the tree
    root = main()

    # print the preorder traversal of the created tree
    printPreOrder(root)
