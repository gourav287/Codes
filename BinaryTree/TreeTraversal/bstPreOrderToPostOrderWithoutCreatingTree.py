"""
The code works to input preOrder of a BinarySearchTree and outputs
the postOrder without actually creating the tree
"""

# The function to print the psot order traversal from the
# given preOrder traversal
def printPostOrder(preOrder, n, minVal, maxVal):

    # The global index to access preOrder elements
    global preIndex

    # If traversed through entire preOrder, just return
    if preIndex == n:

        return

    # Storing the current node in preorder being accessed
    val = preOrder[preIndex]

    # If the current value doesn't fall in Range, just return
    if val < minVal or val > maxVal:

        return

    # Increment the global index
    preIndex += 1

    # Traverse through the left subtree
    printPostOrder(preOrder, n, minVal, val)

    # Traverse through the right subtree
    printPostOrder(preOrder, n, val, maxVal)

    # Print the value
    print(val, end = " ")

# The driver code
if __name__ == '__main__':

    # Input the preOrder list
    preOrder = list(map(int, input().split()))

    # Calculate the length of preOrder
    n = len(vals)

    # Initializing the index of preOrder list
    preIndex = 0

    # Function to print the postOrder traversal from preOrder
    printPostOrder(vals, n, 0, 99999999)
