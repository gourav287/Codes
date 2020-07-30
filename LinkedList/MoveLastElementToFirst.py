"""
This code works on the linked list to convert its last node into first node
"""

# Class for the list nodes
# Each node will be an object of this class
class ListNode:
    
    def __init__(self, data):

        self.data = data

        self.next = None

# Class for the head pointer of list
class LinkedList:

    def __init__(self):

        self.head = None

# Function to insert an element at the end of the list
# Used while creating the list
def insert(start, value):

    node = ListNode(value)

    if not start:

        start = node

    else:
        curr = start

        while curr.next:

            curr = curr.next

        curr.next = node

    return start

# Function to print the entire list
def printlist(start):

    curr = start

    while curr:

        print(curr.data, end = ' ')

        curr = curr.next

    print()

"""
Implementation of the MoveLastNode() function.
"""
def MoveLastNode(start):

    prev = curr = start

    # Traversing till the last node
    # Keeping track of last and second last node
    while curr.next:

        prev = curr

        curr = curr.next

    # Allocating address or original first node into last node's next
    curr.next = start

    # Removing address of next from second last node, making it last
    prev.next = None
    
    # Allocating head pointer to last node, now making it first
    start = curr

    # Returning updated list
    return start

# The driver code
if __name__ == '__main__':

    # Initializing linked list
    start = LinkedList().head

    # Input number of nodes
    n = int(input())

    # Creating the linked list while taking inputs
    for i in range(n):

        start = insert(start, int(input()))

    # Printing the linked list
    printlist(start)

    # Implement last node move
    start = MoveLastNode(start)

    # Printing the updated list
    printlist(start)
