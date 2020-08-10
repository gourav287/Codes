"""
The very first file of this folder tend to focus on
the creation and printing of doubly linked list.
"""

# The node structure
class ListNode:

    def __init__(self, data):

        self.data = data

        self.prev = None

        self.next = None

# Structure, insertion and print function of the linked list as a whole
class LinkedList:

    # Constructor
    def __init__(self):
        
        self.head = None

    # Insertion function named push()
    def push(self, val):

        # Creating a node
        node = ListNode(val)

        # If the list exists
        if self.head:

            # Traverse through the end of list
            curr = self.head
            
            while curr.next:

                curr = curr.next

            # Add node as the new last node of the list
            curr.next = node

            # Update the last node's back pointer
            node.prev = curr
            
        # If list is None
        else:

            # Just create the list
            self.head = node

    # Print function prints the entire list in both orders
    def printlist(self):
        
        curr = self.head

        # Printing the list

        while curr:

            print(curr.data, end = ' ')

            curr = curr.next

        print()

# The main function to create Doubly Linked List and return it's head pointer
def DoublyLinkedList():

    # Input length of the list
    n = int(input())

    # Initialize the list
    start = LinkedList()

    # Input and update nodes in the list
    for _ in range(n):

        val = int(input())

        start.push(val)

    # Returning the head pointer of doubly linked list
    return start


# The driver code
if __name__ == '__main__':

    # Calling the function to create the doubly linked list
    start = DoublyLinkedList()

    # Print the entire list
    start.printlist()
