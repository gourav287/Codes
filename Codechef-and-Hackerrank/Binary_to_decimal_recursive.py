# -*- coding: utf-8 -*-
"""
Write a recursive code to convert binary string into decimal number
"""

# The working function
def bin2deci(binary, i = 0):
    
    # Calculate length of the string
    n = len(binary)
    
    # If string has been traversed entirely, just return
    if i == n - 1:
        
        return int(binary[i])
    
    # Left shifting i-th value to n-i-1 positions will actually multiply
    # it with 2**(n-i-1) This will then be added to values at other i
    # and final solution will be returned
    return ((int(binary[i])<<(n-i-1)) + bin2deci(binary, i + 1))

# The driver code
if __name__ == "__main__":
    
    # Input the string
    binary = input()
    
    # Print the output
    print(bin2deci(binary))