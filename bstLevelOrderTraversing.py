"""
Question Link:
https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
"""

#Solution:

#The node class
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

#The program you need to write in this problem
def levelOrder(root):
    q = [root]
    while q:
        n = q.pop(0)
        print (n.info, end = ' ')
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)

#The driver Code
if __name__ == '__main__':
    
    tree = BinarySearchTree()
    t = int(input())

    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    levelOrder(tree.root)
