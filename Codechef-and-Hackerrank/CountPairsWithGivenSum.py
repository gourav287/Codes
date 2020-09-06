# -*- coding: utf-8 -*-
# Question link:
#   https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum/0
"""
Given an array of integers, and an integer  ‘K’ , find the count of pairs of
elements in the array whose sum is equal to 'K'.
"""

'''
The efficient approach is to use hashing (using array or dictionary in python)
It works under the time complexity O(n)
'''
def countPairs(arr, k):
    
    # Initialize the empty hashing dictionary and the count value = 0
    hash_, cnt = {}, 0
    
    # For each value in arr, we will check if the required value is
    # present in the dictionary
    for i in arr:
        
        val = k - i
        
        # If value is present, add it's count as that many pairs can be formed
        if hash_.get(val, -1) >= 0:
            
            cnt += hash_[val]
        
        # Also append/increment the current arr value to be checked in future
        if hash_.get(i, -1) >= 0:
            
            hash_[i] += 1
        
        else:
            
            hash_[i] = 1
    
    # Return the count value
    return cnt

# The driver code
if __name__ == "__main__":
    
    # no of test cases
    t = int(input())
    
    # For each iteration
    for _ in range(t):
        
        # Length of array and value of sum
        n, k = map(int, input().split())
        
        # input the array
        arr = list(map(int, input().split()))
        
        # Call te function to calculate the required count and print its value
        print(countPairs(arr, k))