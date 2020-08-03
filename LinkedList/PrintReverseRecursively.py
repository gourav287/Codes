"""
Implementation to print a list recursively without actually reversing the list
"""

# Class for the list nodes
# Each node will be an object of this class
class ListNode:

    def __init__(self, data):

        self.data = data

        self.next = None

# The main class defining each linked list
class LinkedList:

    def __init__(self):
        self.head = None

    # Inserting new nodes in the linked list object
    def push(self, val):
        node = ListNode(val)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    # Printing all the values of the linked list object
    def printlist(self):
        curr = self.head
        while curr:
            print(curr.data, end = ' ')
            curr = curr.next
        print()
        
"""
Implementation of ReversePrint function, to print the values
in reverse order, without reversing the actual list
"""
def ReversePrint(start):

    # Return if reached the end
    if start == None:
        
        return

    # Recursive call to the next node
    ReversePrint(start.next)

    # Print the value
    print(start.data, end = " ")


# The driver code
if __name__ == '__main__':

    # Initializing both linked lists
    start = LinkedList()

    # Input number of nodes in both lists
    n = int(input())

    # Entering values of the list
    for _ in range(n):

        start.push(int(input()))

    # Printing the original list
    print("Original list:", end = " ")
    start.printlist()

    # Calling the function to print values in reverse order
    print("The reversed values are:", end = " ")
    ReversePrint(start.head)
