# -*- coding: utf-8 -*-
"""
Question Link:
    https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

Given two strings, a and b, that may or may not be of the same length, determine
the minimum number of character deletions required to make a and b anagrams. 
Any characters can be deleted from either of the strings.

For example, if a=cde and b=dcf, we can delete e from string a and f from string b
so that both remaining strings are  and  which are anagrams.
"""

# Importing the necessary library
from collections import Counter

# Function to return required value
def makeAnagram(a, b):

    # Making Counter object for both the strings
    ct_a = Counter(a)
    ct_b = Counter(b)

    # This will remove all the duplicates and add 
    # extra elements of ct_b with negative values.
    ct_a.subtract(ct_b)
    
    # The count of all the elements in the ct_a is the number
    # of elements we need to delete from the strings.
    return sum(abs(i) for i in ct_a.values())


# The driver code
if __name__ == '__main__':
    
    # Input string 1
    a = input()
    
    # Input string 2
    b = input()

    # Getting the desired count by the makeAnagram() function
    res = makeAnagram(a, b)
    
    # Printing the solution
    print(res)