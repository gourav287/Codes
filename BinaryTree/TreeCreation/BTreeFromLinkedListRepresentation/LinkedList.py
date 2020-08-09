"""
This part of code contains implementation of linked list creation.

This file will be used as a module for the main file that creates

binary tree from the linked list implementation
"""

# Class to create the linked list node
class ListNode:

    # Contains data and the link to next element
    def __init__(self, data):

        self.data = data

        self.next = None

# Class denoting the linked list and containing
# the function for creation of linked list
class LinkedList:

    def __init__(self):

        self.head = None

    # Function to push a new node at the end of the list
    def push(self, val):

        node = ListNode(val)

        # IF list does not exist, just create it
        if not self.head:

            self.head = node

        # Else move to the last node and connect the new node there
        else:

            curr = self.head

            while curr.next:

                curr = curr.next

            curr.next = node

# Function to print the list
def printList(head):

    curr = head

    # Iterate through the entire list and keep printing every element
    while curr:

        print(curr.data, end = " ")

        curr = curr.next

    print()

# function to be called from main to create the list
def createList():

    # Input length of the list
    n = int(input())

    # Input all the n-values in the list.
    # Will ignore other values if more than n are input
    vals = list(map(int, input().split())) [ : n]
    
    # Create a LinkedList object
    start = LinkedList()

    # Iterate through the values and keep pushing them into the list
    for val in vals:

        start.push(val)

    # Return the created linked list's head pointer
    return start.head

# The driver code of this file
if __name__ == "__main__":

    # Create the linked list
    start = createList()

    # Print the created list
    printList(start)
