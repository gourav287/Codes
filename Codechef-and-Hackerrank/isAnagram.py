# -*- coding: utf-8 -*-
"""
Question Link:
    https://practice.geeksforgeeks.org/problems/anagram/0
    
Given two strings a and b consisting of lowercase characters. The task
 is to check whether two given strings are anagram of each other or not.
"""

# The driver code
if __name__ == "__main__":
	
	# For all the test cases
    for _ in range(int(input())):
        
        # Input the strings
        a, b = input().split()
        
        # Create an array to store count of all alphabets
        arr = [0 for i in range(26)]
        
        # Get the count of alphabets in string 1
        for i in a:
            
            arr[ord(i)-97] += 1
        
        # Delete the count of alphabets in b from that in a
        for i in b:
            
            arr[ord(i)-97] -= 1
        
        # For any alphabet
        for i in range(26):
            # If the count is not zero, its not an anagram
            if arr[i] != 0 :
                
                print("NO")
                
                break
        
        # If the count is zero for all alphabets
        else:
            
            print("YES")