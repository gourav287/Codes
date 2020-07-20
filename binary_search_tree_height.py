"""
Question Link:
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
"""

#Solution:

#Node class to determine properties of each node
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

#The class responsible for the Binary Search Tree
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


#The part you need to code
                #STARTS

#A perfect recursive approach to determine correct height of Binary Tree
def height(root):
    return 1 + max(height(root.left), height(root.right)) if root else -1

                #ENDS


if __name__ == '__main__':
    
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    print(height(tree.root))
