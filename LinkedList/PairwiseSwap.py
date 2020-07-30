"""
this file contains implementation of pairwise swapping
of all the data in a linked list
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
Implementation of pairwise swapping
"""
def Swapping(start):

    curr = start

    # Swap each pair until possible
    while curr and curr.next:
        
        curr.data, curr.next.data = curr.next.data, curr.data

        curr = curr.next.next

    # return the updated linked list
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

    start = Swapping(start)

    printlist(start)
