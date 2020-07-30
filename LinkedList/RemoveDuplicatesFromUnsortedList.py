"""Program to remove nodes with duplicate values
from an unsorted list

The algorithm uses hashing (by dictionary) and works in O(n) space and time
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
This is the implementation of removing duplicate values from the unsorted list
"""
def RemoveDuplicates(start):

    # No duplicates if length is less than 2
    if start == None or start.next == None:

        return start

    # Back to back pointers to skip the duplicate nodes
    backptr, forptr = start, start.next

    # Storing the traversed values
    dicti = {backptr.data:1}

    # Traversing through the list
    while forptr:

        # If the value is already traversed, skip the node
        if dicti.get(forptr.data):

            backptr.next = forptr.next

        # Else update the dictionary and move on
        else:
            
            backptr = forptr

            dicti[forptr.data] = 1
        
        forptr = forptr.next

    # Returning updated linked list
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

    # Removing the duplicates
    start = RemoveDuplicates(start)

    # Printing the updated list with non duplicate values
    printlist(start)
