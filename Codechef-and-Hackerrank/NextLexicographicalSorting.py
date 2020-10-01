# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:08:03 2020

Implement next permutation, which rearranges numbers into the 
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest 
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its 
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

# Function to create the next lexicographical permutation of array
def Sorting(arr, n):
    
    # Traverse from the last element to find the first element not in decreasing order
    i = n - 1
    
    while i > 0 and arr[i] < arr[i - 1]:
        
        i -= 1
    
    # Traverse from last to find the element we need to replace with ith element
    j = n - 1
    
    while j >= 0 and arr[j] < arr[i - 1]:
        
        j -= 1
    
    # Swap ith and jth element
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Sort the elements from ith index to last
    newarr = sorted(arr[i:])
    
    # Array till ith index is same, after ith index is sorted now
    # So that the new array is lexicographically next sorted to the 
    # previous one
    arr = arr[:i]
    arr.extend(newarr)
    
    # Return the array
    return arr

# The driver code
if __name__ == "__main__":
    
    # For no of test cases
    for _ in range(int(input())):
        
        # Input the length of the array
        n = int(input())
    
        # Input the number array
        arr = list(map(int, input().split()))
        
        # Function to implement next lexicographical sorting
        arr = Sorting(arr, len(arr))
        
        # Printing the array
        print(*arr)
