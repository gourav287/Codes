# -*- coding: utf-8 -*-
"""
Question link :
    https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
"""

# The driver code
if __name__ == "__main__":
	
    # For t test cases
    for _ in range(int(input())):
        
        # Input the string
        s = input()
        
        # comvert into an array of all words
        arr = s.split(".")
        
        # Reverse each individual word
        for i in range(len(arr)):
            
            arr[i] = arr[i][::-1]
        
        # Join the words in array to form a string with . in between
        s = '.'.join(arr)
        
        # Reverse the string
        s = s[::-1]
        
        # The current form of string is the required output
        print(s)