"""
Program to return merging point of two linked lists if found
"""
# Random library to create runtime random merging point
from random import randint

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

    # Intersecting 2 linked list at a random node
    def intersect(self, obj, n):

        curr1 = self.head
        curr2 = obj.head
        while curr2.next:
            curr2 = curr2.next
        for _ in range(n):
            curr1 = curr1.next

        curr2.next = curr1

"""
Function to return merging point of 2 linked lists
"""
def IntersectionPoint(start1, start2):

    # Initializing temporary pointers
    curr1, curr2 = start1, start2

    # Check variables for no intersection condition
    flag1, flag2 = 0, 0

    while 1:
        
        # If intersection point is found, just return it
        if curr1 == curr2:

            return curr1.data

        # Either keep iterating, or change pointed list
        if curr1.next:

            curr1 = curr1.next

        else:

            # If curr1 iterated once through both lists and intersection
            # is not found, the intersection doesn't exist
            if flag1 == 1:

                return -1

            # Let curr1 iterate through 2nd list now
            curr1 = start2

            flag1 = 1
            
        # Either keep iterating, or change pointed list
        if curr2.next:

            curr2 = curr2.next

        else:

            # If curr2 iterated once through both lists and intersection
            #is not found, the intersection doesn't exist
            if flag2 == 1:

                return -1

            # Let curr2 iterate through first list now
            curr2 = start1

            flag2 = 1

    return -1

if __name__ == '__main__':

    # Initializing both linked lists
    start1, start2 = LinkedList(), LinkedList()

    # Input number of nodes in both lists
    n, m = map(int, input().split())

    # Entering values of 1st list
    for _ in range(n):
        val = int(input())
        start1.push(val)

    # Entering values of 2nd list
    for _ in range(m):
        val = int(input())
        start2.push(val)

    # Making the end of 2nd list join a random node in 1st list
    # This will make the 2 lists intersect
    inte = randint(1, n)
    start1.intersect(start2, inte)

    # Calling the function to find the node where intersection took place
    val = IntersectionPoint(start1.head, start2.head)

    # Print list1 and list2
    print("List1:", end = " ")
    start1.printlist()
    print("List2:", end = " ")
    start2.printlist()

    # Print the data on the intersection point
    print("\nIntersection found on node valued {}".format(val)\
          if val != -1 else "\nIntersection not found")
