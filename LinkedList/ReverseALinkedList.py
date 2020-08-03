"""
Implementation of reversal of linked list iteratively in O(n) time.
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
Implementation of Reverse function, to change all the links of the nodes,
and eventually reverse the entire list.
"""
def Reverse(start):

    # NULL list or List with only one node do not need reversal
    if not start or not start.next:

        return start

    # Initializing variable pointers
    prev, curr = None, start

    # Iterating through the list
    while curr:

        # Temporarily storing next node address
        tmp = curr.next

        # Reversing the node link
        curr.next = prev

        # Moving forward
        prev = curr

        curr = tmp

    # Updating the head value
    start = prev

    # Returning the head value to driver code
    return start


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

    # Calling the function to reverse the linked list
    start.head = Reverse(start.head)

    # Printing the updated/reversed list
    print("Reversed list:", end = " ")
    start.printlist()
