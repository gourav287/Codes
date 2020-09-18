# -*- coding: utf-8 -*-
# Question Link:
    #https://practice.geeksforgeeks.org/problems/non-repeating-element/0
"""
Find the first non-repeating element in a given array A of N integers.
Note: Array consists of only positive and negative integers and not zero.
"""

# For t test cases
for _ in range(int(input())):
    
    # No of elements in array
    n = int(input())
    
    # Inputting the array
    arr = list(map(int, input().split()))
    
    # Initializing a dictionary, to implement hashing
    myd = {}
    
    # Storing count of each element
    for i in arr:
        
        try:
            
            myd[i] += 1
        
        except:
            
            myd[i] = 1
    
    # First element with count = 1 is the answer
    for i in arr:
        
        if myd[i] == 1:
            
            print(i)
            
            break