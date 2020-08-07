"""
Implementation of code to print post order of a binary tree
when preorder and inorder traversal are given
"""

# Class to create a tree node
class Node:

    def __init__(self, data):

        # Contains data and link for both child nodes
        self.data = data
        
        self.left = None

        self.right = None

"""
Program to print postOrder traversal of the tree when
inOrder and preOrder traversals are given
"""
def printpost(inOrder, preOrder, left, right):

    # A global variable to keep track of current preOrder element
    global cur_ind

    # If no element in the desired subtree, simply return
    if left > right:

        return
    
    # store value of the current node
    val = preOrder[cur_ind]

    # Find index of the element in inorder
    ind = inOrder.index(val)

    # Increment the preOrder index
    cur_ind += 1

    # Access left subtree
    printpost(inOrder, preOrder, left, ind - 1)

    # Access right subtree
    printpost(inOrder, preOrder, ind + 1, right)

    # Print value of the current node
    print(val, end = " ")
    

# The driver code
if __name__ == '__main__':

    # inOrder traversal of the tree
    inOrder = list(map(int, input().split())) #[1, 2, 3, 4, 5, 6, 7]

    # preOrder traversal of the tree
    preOrder = list(map(int, input().split())) #[4, 2, 1, 3, 6, 5, 7]

    # Index to keep track of preOrder elements
    cur_ind = 0

    # printing postOrder without creating a tree
    # Given preOder and inOrder
    print("Post order traversal is:")
    printpost(inOrder, preOrder, 0, len(inOrder) - 1)
