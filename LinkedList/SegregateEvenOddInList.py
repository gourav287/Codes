"""
The code modifies a linked list to segregate even and odd valued nodes
The order of even nodes and odd nodes in themselves remain unchanged
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
Implementation of Segregate function, to separate even and odd valued nodes
We will create 2 linked lists for even and odd values and then merge them
"""
def Segregate (start):

    # List with no or single node doesn't need any checking
    if not start or not start.next:

        return

    # Pointer to iterate through list
    curr = start

    # Creating separate lists for even and odd values and their current pointers
    even, odd = LinkedList(), LinkedList()
    even_curr = even.head
    odd_curr = odd.head

    # Iterating through primary list
    while curr:

        # Creating a new node
        node = ListNode(curr.data)

        # If the value is even
        if node.data % 2 == 0:

            # If list exist, append value at the last
            if even.head:

                even_curr.next = node

                even_curr = even_curr.next

            # Appending the list's first node
            else:

                even.head = even_curr = node

        # If the node value is odd
        else:

            # If list exist, append value at the last
            if odd.head:

                odd_curr.next = node

                odd_curr = odd_curr.next

            # Appending the list's first node
            else:

                odd.head = odd_curr = node

        # Move to the next node in main list
        curr = curr.next

    # Append odd list after even, if even exists. Hence list is segregated
    if even.head:
        
        even_curr.next = odd.head

    # When the list only had odd values
    else:

        even = odd
    
    # Return the segregated list
    return even

# The driver code
if __name__ == '__main__':

    # Initializing both linked lists
    start = LinkedList()

    # Input number of nodes in both lists
    n = int(input())

    # Entering values of 1st list
    for _ in range(n):

        val = int(input())

        start.push(val)

    # Printing the original list
    print("Original list:", end = " ")
    start.printlist()

    # Function to segregate even and odd numbers separately
    start = Segregate(start.head)

    # Printing the updated list
    print("Updated list:", end = " ")
    start.printlist()
