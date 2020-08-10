"""
This piece of code contains implementation of doubly linked list and
reversal of the list
"""

# The node structure through a class
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

    # Print function prints the entire list
    def printlist(self):
        
        curr = self.head

        if not curr:

            print("List does not exist\n")

            return

        # Printing the list in forward order
        while curr:

            print(curr.data, end = ' ')

            curr = curr.next

        print("\n")

"""
Implementation of Reversal of Doubly Linked List
"""
def ReverseNode(start):

    # Check if list exists and has more than 1 elements else do nothing
    if start and start.next:

        # Initialize a pointer, initially pointing to the head of the list
        cur_node = start

        # Traversing through the list
        while cur_node:
            
            # Interchange current node's prev and next pointers in single step
            cur_node.prev, cur_node.next = cur_node.next, cur_node.prev

            # Move the pointer to next node if possible !
            # We have used cur_node.prev because the references have
            # been interchanged. Now prev is next and next is prev
            if cur_node.prev:
                
                cur_node = cur_node.prev

            # Else break loop if at the last node already
            else:
                
                break

        # Assign head pointer to the last node which is now the first one
        start = cur_node

    # Return head pointer
    return start


# The driver code
if __name__ == '__main__':

    # Input length of the list
    n = int(input())

    # Initialize the list
    start = LinkedList()

    # Input and update nodes in the list
    for _ in range(n):

        val = int(input())

        start.push(val)

    # Print the entire list
    print("Original list:")
    start.printlist()

    # Reversing the list
    start.head = ReverseNode(start.head)

    # Printing the updated list
    print("Reversed list:")
    start.printlist()
