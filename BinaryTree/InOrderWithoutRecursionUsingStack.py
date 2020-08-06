"""
Implementation of inOrder traversal of a tree
The traversal is implemented iteratively with the help of a stack
"""

# Importing the already created code for tree creation
# This lets us focus on the specific task in this file
# Check file with the module name in the same folder
import BinaryTreeCreation as BTC

"""
InOrder Traversal through stack
"""
def InOrderByStack(root):

    # Initialize stack
    st = []

    # Initialize a pointer to the root of tree
    curr = root

    # Iterating through tree and stack together
    while True:

        # If current pointer is not NULL keep reaching left child
        if curr :

            # Placing pointer to the tree node into stack
            # before leaving it
            st.append(curr)

            curr = curr.left

        # If reached the left leaf node
        # Backtrack from empty subtree and visit the Node
        # at top of Stack
        elif st:

            node = st.pop()

            print(node.data, end = " ")

            curr = node.right

        # If current pointer is NULL and stack is empty
        # Means we traversed the entire tree now so stop
        else:

            break

    # Simply printing the nextLine for output looks
    print()

# The driver code
if __name__ == "__main__":

    # Creating the simple Binary Tree
    root = BTC.BinaryTree()

    # Calling function to traverse inOrder iterativey using stack
    InOrderByStack(root)
