"""
This piece of code contains implementation of doubly linked list and
reversal of the list
"""

# Importing the already created module from the same folder
# It contains code for creation of doubly linked list
# This will let us create the doubly linked list without
# writing code for it in this file
from DoublyCreation import *


"""
Implementation of Reversal of Doubly Linked List
"""
def ReverseNode(start):

    # Check if list exists and has more than 1 elements else do nothing
    if start and start.next:

        # Initialize a pointer, initially pointing to the head of the list
        cur_node = start

        # Traversing through the list
        while cur_node:
            
            # Interchange current nodes prev and next pointers in single step
            cur_node.prev, cur_node.next = cur_node.next, cur_node.prev

            # Move the pointer to next node if possible !
            # We have used cur_node.prev because the references have
            # been interchanged. Now prev is next and next is prev
            if cur_node.prev:
                
                cur_node = cur_node.prev

            # Else break loop if at the last node already
            else:
                
                break

        # Work separately for the last node
        # cur_node.prev, cur_node.next = cur_node.next, cur_node.prev

        # Assign head pointer to the last node which is now the first
        start = cur_node

    # Return head pointer
    return start


# The driver code
if __name__ == '__main__':

    # Creating the doubly linked list
    start = DoublyLinkedList()

    # Print the entire list
    print("Original list:")
    start.printlist()

    # Reversing the list
    start.head = ReverseNode(start.head)

    # Printing the updated list
    print("Reversed list:")
    start.printlist()
    
