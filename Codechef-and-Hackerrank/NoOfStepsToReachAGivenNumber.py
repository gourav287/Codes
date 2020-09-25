# -*- coding: utf-8 -*-
"""
Question Link:
    https://practice.geeksforgeeks.org/problems/minimum-number-of-steps-to-reach-a-given-number5234/1

Given an infinite number line.  You start at 0 and can go either to the left or to the right. 
The condition is that in the ith move, youmust take i steps. 
Given a destination D , find the minimum number of steps required to reach that destination.
"""

# Function to calculate minimum no of steps
def minSteps(self, D):
    
    # Initializing source to track current place
    source = 0
    # i will track the length of next move
    i = 1
    
    # Keep going forward as it will minimize steps
    while source < D:
        source += i
        i += 1
    
    # Distance remaining to reach 
    diff = source - D
    
    # If distance remaining is odd, we need to make it even
    while diff % 2 != 0:
        
        source += i
        diff = source - D
        i += 1
    
    # If distance is even, it means altering a few steps taken will
    # lead us to destination, hence this is the answer
    return i - 1

# Driver Code
if __name__ == '__main__':
    
    # No of test cases
    for _ in range(int(input())):
        
        # Destination
        D = int(input())
        
        #Calling the required function
        print(minSteps(D))