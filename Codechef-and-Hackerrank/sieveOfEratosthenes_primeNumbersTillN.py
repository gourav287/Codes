# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:06:04 2020

@author: snsax
"""

# The solution class, as given in the code section
class Solution:
    
    # Function to implement sieve of eratosthenes method to find list of all prime numbers
    # upto given number n. Complexity = O ( n * log ( log ( n ) ) )
    def sieveOfEratosthenes(self, n):
        
        # Declare and array of n+1 elements
        arr = [True for i in range(n+1)]
        
        arr[0], arr[1] = False, False
        
        # Iterate through the array
        for i in range(2, n+1):
    	    
    	    # If number i is not the multiple of any number,
    	    # mark the all multiples of i in the list
    	    if arr[i] == True:
    	        
    	        for j in range(i*i, n+1, i):
    	            
    	            arr[j] = False
    	
    	# The numbers which are left unmarked are the prime numbers    
        lis = []
    	
    	# So append all the prime numbers
        for i in range(n + 1):
    	    
            if arr[i] == True:
                
                lis.append(i)
    	
    	# Return the list of all the prime numbers upto n
        return (lis)

# The driver code
if __name__ == '__main__': 
    
    # Number of test cases
    t = int(input())
    
    for _ in range(t):
        
        # Input the number
        N = int(input())
        
        # Creating the object of the Solution class
        ob = Solution()
        
        # Calling the required function
        ans = ob.sieveOfEratosthenes(N)
        
        # print the list of all prime numbers till n
        for i in ans:
            
            print(i, end=" ")
        
        print()