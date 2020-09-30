# -*- coding: utf-8 -*-
"""
Question Link:
    https://practice.geeksforgeeks.org/problems/remove-repeated-digits-in-a-given-number/0/?category[]=Stack&difficulty[]=-1&page=1&query=category[]Stackdifficulty[]-1page1

Given an integer N, remove consecutive repeated digits from it.
"""

#code
def removeConsecutiveRepeated(a):
    
    # Initialize the stack
    stack = [a%10]
    a = a//10
    
    # Traverse through every digit of the number
    while a > 0:
        
        # Store it if it's not consecutively duplicate
        # i.e., not present at the top of the stack
        rem = a%10
        
        if stack[-1] != rem:
            
            stack.append(rem)
        
        a = a//10
    
    # Initialize a number n
    n = 0
    
    # Pop out the stack elements and create the required number from them
    while stack:
        
        val = stack.pop(-1)
        
        n = 10*n + val
    
    # Print the resultant number
    print(n)
    
# The driver code
if __name__ == "__main__":
	
    # For t test cases
    for _ in range(int(input())):
        
        # Input the number
        n = int(input())
        
        # Call the required number
        removeConsecutiveRepeated(n)