"""
Implementated deletion of n-th numbered node from
the doubly linked list
Simply iterate till the node, change pointer values of
previous and next node and then free the node
"""

# Importing creation code to save from writing it again
from DoublyCreation import *

"""
function to delete nth node
"""
def DeleteNthNode(start, n):

    # Do nothing if the list is empty
    if start.head == None:

        return start

    # Deleting the head element if n == 1
    if n == 1:

        start.head = start.head.next

        start.head.prev = None

        return start

    # Set a pointer to the head of the node
    curr = start.head

    # Iterate through the node to reach the desired node
    for i in range(n-1):

        if curr.next:

            curr = curr.next

        # If list is shorter than n, can't delete anything so return
        else:

            print("List index out of range ! ")

            return start

    # Change pointers of the previous node to point the next and vice versa
    curr.prev.next = curr.next

    if curr.next:

        curr.next.prev = curr.prev

    return start
    
# The main function
if __name__ == "__main__":

    start = DoublyLinkedList()

    n = int(input())

    print("List before deletion:", end = " ")
    start.printlist()

    start = DeleteNthNode(start, n)

    print("List after deletion:", end = " ")
    start.printlist()
