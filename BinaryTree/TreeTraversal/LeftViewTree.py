"""
Implement the code to get the left view of the binary-tree

The logic is to traverse every node left and right child and check
if any element has been printed at that level of the tree
This is checked by keeping track of the biggest level whose
leftmost element is already printed
"""

# Making the file look into it's parent folder's subdirectories
# for modules using sys.path
import sys
sys.path.append('../')

# Importing the already created code for tree creation
# This lets us focus on the specific task in this file
# Check folder with the module name in the parent folder
import TreeCreation.SimpleBinaryTree as SBT



# LeftViewUtil function to print the left view of the tree
def LeftViewUtil(root, level, maxLevel):

    # If node is null, just return
    if not root:

        return

    # If the current level is not traversed even once
    # Print the traversed data and update 'traversed' in the maxLevel
    if level > maxLevel[0]:

        print(root.data, end = " ")

        maxLevel[0] = level

    # Traverse through both the children of the node, left first
    LeftViewUtil(root.left, level + 1, maxLevel)

    LeftViewUtil(root.right, level + 1, maxLevel)

"""
Implementing the desired function to get the left view of the tree
"""
def LeftView(root):

    # To keep track of maximum level whose element is printed
    maxLevel = [0]

    # Function to print the left view of the tree
    LeftViewUtil(root, 1, maxLevel)



# The driver code
if __name__ == "__main__":

    # Creating the simple Binary Tree
    root = SBT.BinaryTree()

    # Calling function to traverse inOrder iterativey using stack
    print("Left side view of the tree is : ")
    LeftView(root)
