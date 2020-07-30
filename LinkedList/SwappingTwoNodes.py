"""
This piece of code contains implementation of swapping two links of given data value
It swaps the node itself, and not the data

For now, it is assumed that,
the nodes to be swapped does not include the start node
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
This is the implementation of node swapping
"""
def SwappingNodes(start, x, y):

    if x == y:

        return start

    ptr1 = ptr2 = None

    curr = start

    # Iterate to get to the nodes previous to the nodes which are to be swapped
    while curr.next:

        if curr.next.data == x:

            ptr1 = curr

        if curr.next.data == y:

            ptr2 = curr

        curr = curr.next

    # If both nodes exist, swap them
    if ptr1 and ptr2:

        ptr1.next, ptr2.next = ptr2.next, ptr1.next

        ptr1.next.next, ptr2.next.next = ptr2.next.next, ptr1.next.next

    # Return updated linked list
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

    # Insert values of nodes to be swapped
    x = int(input())

    y = int(input())

    # Printing the linked list
    printlist(start)

    # Swapping the nodes
    start = SwappingNodes(start, x, y)

    # Printing the updated list
    printlist(start)
