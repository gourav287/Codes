"""
This file contains code to check if the linked list contains any loop
"""

# Import random integer from random module
from random import randint

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

# This function if called, creates a loop in the linked list
def initiateloop(start):

    if start == None:

        print("List will not have looping.")

        return start

    curr = start

    while curr.next:
        curr = curr.next

    curr.next = start

    print("List will have looping")

    return start

"""
The code to check looping in the list :
"""
def loopCheck(start):
    
    # Initialize 2 pointers at starting node
    prev = curr = start

    # flag to check if loop exist or not
    flag = False

    # Looping till the end or till the looping is detected
    while curr != None and curr.next != None:

        curr = curr.next.next

        prev = prev.next

        if curr == prev:

            flag = True

            break

    # If the end is found means there's no loop
    if curr == None or curr.next == None:

        flag = False

    # Return status of list: looped/unlooped
    return flag

# The driver code
if __name__ == '__main__':

    # Initializing linked list
    start = LinkedList().head

    # Input number of nodes
    n = int(input())

    # Creating the linked list while taking inputs
    for i in range(n):

        start = insert(start, int(input()))

    # Looping created/not created randomly
    ran = randint(0,1)

    if ran == 1:
        
        start = initiateloop(start)

    else:

        print("List will not have looping.")

    #Call the function to get the value
    if loopCheck(start):

        print("Our function says: Loop exists in the list")

    else:

        print("Our function says: Loop doesn't exist in the list")

