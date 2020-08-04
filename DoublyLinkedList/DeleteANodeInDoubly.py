"""
This piece of code contains implementation of doubly linked list and
deletion of any given list node from the list
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
Implementation of node deletion
"""
def DeleteNode(start, nodeval):

    # Check if list exists
    if not start:

        print("Can't delete from an empty list\n")

    else:

        # Traverse till the node is found or list ends
        curr = start

        while curr:

            # If the node is found
            if curr.data == nodeval:

                # If the node is the head node
                if curr == start:

                    start = curr.next

                    curr.next.prev = None

                # If the node is the last node
                elif curr.next == None:

                    curr.prev.next = None

                    curr.prev = None

                # For any other node
                else:

                    curr.prev.next = curr.next

                    curr.next.prev = curr.prev

                break

            curr = curr.next

        # If the node is not found in the list
        else:

            print("Node not found in the list\n")

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

    # Input the nodeval to delete
    nodeval = int(input())

    # Print the entire list
    print("Original list:")
    start.printlist()

    # Deleting a node
    start.head = DeleteNode(start.head, nodeval)

    # Printing the updated list
    print("Updated list:")
    start.printlist()
