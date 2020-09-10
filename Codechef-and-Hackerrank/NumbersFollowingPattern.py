# -*- coding: utf-8 -*-
# Question link:
  # https://practice.geeksforgeeks.org/problems/number-following-a-pattern/0
"""
Given a pattern containing only I's and D's.
I for increasing and D for decreasing.
Devise an algorithm to print the minimum number following that pattern.
Digits from 1-9 and digits can't repeat.
Example:
    Input :    IIDIII
    Output :   1243567
    
    Input :    DDIDII
    Output :   3215467

"""
"""
Approach:
    Create a stack where we will store consecutive increasing numbers up until
    we keep receiving 'D' in the pattern.
    Once we get an 'I' or the pattern ends, we will pop everythin out and
    the output will be in same numbers of decreasing elements as there were
    consecutive 'D'.
    
    All of this will be done by iterating from i = 0 to length of pattern.
    
    This way not only will the digits in the number follow the pattern,
    they will also be unique.

"""
# Function to return the number following the given pattern
def Pattern(inp):
    
    # Initialize a stack
    stack = []
    
    # Initialize the value of number
    val = 0
    
    # Iterating for n numbers
    for i in range(len(inp) + 1):
        
        # Insertion in stack
        stack.insert(0, i+1)
        
        # Condition for the popping
        if i == len(inp) or inp[i] == 'I':
            
            while stack != []:
                
                val = 10 * val + stack.pop(0)
    
    # Return the required number
    return val

# The driver code
if __name__ == "__main__":
    
    # No of test cases
    t = int(input())
    
    for _ in range(t):
        
        # Input the pattern
        inp = input()
        
        # Calling Pattern function to print the number following the pattern
        print(Pattern(inp))