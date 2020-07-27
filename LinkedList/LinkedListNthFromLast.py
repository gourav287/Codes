"""
This file contains code to find the nth node
from the last of a single linked list
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


"""
The code for nth node from the last :
"""
def nthfromlast(start, n):
    
    # Initialize 2 pointers at starting node
    prev = curr = start

    # Traverse curr pointer to the nth node if possible
    while curr != None and n > 0:

        curr = curr.next

        n -= 1

    # This occurs if length of list is less than n
    if n > 0:
        return

    # Traverse both pointers until one of them is null
    # This will ensure that the other pointer is n steps away from the last
    while curr != None:
        
        curr = curr.next

        prev = prev.next

    # Return the data of the desired pointer
    return prev.data


# Function to print the entire list
def printlist(start):

    curr = start

    while curr:

        print(curr.data, end = ' ')

        curr = curr.next

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

    # Input the index from last whose value we want
    nth = int(input('\n'))

    #Call the function to get the value
    val = nthfromlast(start, nth)

    # Output the value
    if val == None:
        print("The node doesn't exist.")
    else:
        print("element no. {} from last is {}".format(nth, val))
