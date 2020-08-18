"""
This file contains code to check if a path sum in tree is equal to
a given value

First input the tree and the sum value
Check every path from root to leaf to check if sum of elements on
any path is equal to the given sum or not.
"""

# Making the file look into it's parent folder's subdirectories
# for modules using sys.path
import sys
sys.path.append('../')

# Importing the already created code for tree creation
# This lets us focus on the specific task in this file
# Check folder with the module name in the parent folder
import TreeCreation.SimpleBinaryTree as SBT

"""
Function to check if any path contains the given sum
"""
def isPath(root, n, csum):

    # If we crossed the leaf node, just check for sum
    if not root:

        if n == csum:

            return True

        else:

            return False

    val = int(root.data)

    # Traverse to left child
    flag = isPath(root.left, n, csum + val)

    # Traverse to right child if left could not give required sum
    if not flag:
        
        flag = isPath(root.right, n, csum + val)

    # Return if the path required is found or not
    return flag

# The driver code
if __name__ == "__main__":

    # Creating the simple binary tree
    root = SBT.BinaryTree()

    # Input the value of sum to be compared to
    n = int(input())
    
    # Check if the tree has a path from root to leaf adding upto n
    path = isPath(root, n, 0)
    
    # Print if the path exist or not
    if path:

        print("Yes the path exist")

    else:

        print("No the path does not exist")
