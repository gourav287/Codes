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
Implementation of the Intersecting function
"""
def Intersection(start1, start2):

    # Initializing the new linked list
    start3 = LinkedList().head
    curr = start3

    # Iterating till at least one list ends
    while start1 and start2:

        # Add node if present in both
        if start1.data == start2.data:

            node = ListNode(start1.data)

            # If the list isn't initialized yet
            if not start3:

                curr = start3 = node

            # Update the new node with common values
            else:

                curr.next = node

                curr = curr.next

            # Keep iterating then
            start1 = start1.next

            start2 = start2.next

        # Keeping iterating through smaller valued list as
        # list values are sorted
        elif start1.data < start2.data:

            start1 = start1.next

        else:

            start2 = start2.next

    # Return the intersectioned list
    return start3

# The driver code
if __name__ == '__main__':

    # Initializing linked list
    start1 = LinkedList().head
    start2 = LinkedList().head

    # Input number of nodes
    n = int(input())

    # Creating the linked list while taking inputs
    for i in range(n):

        start1 = insert(start1, int(input()))

    # Input number of nodes
    n = int(input())

    # Creating the linked list while taking inputs
    for i in range(n):

        start2 = insert(start2, int(input()))

    start3 = Intersection(start1, start2)

    # Printing the linked list
    printlist(start3)
