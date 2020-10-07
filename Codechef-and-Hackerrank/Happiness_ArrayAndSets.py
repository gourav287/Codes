# -*- coding: utf-8 -*-
"""
Question link:
    https://www.hackerrank.com/challenges/no-idea/problem
    
"""

# Input size of array and sets
n, m = map(int, input().split())

# input the array
ar = input().split()

# Input both the sets
a = set(input().split())
b = set(input().split())

# calculate and print the required value of happiness
print(sum([(i in a) - (i in b) for i in ar]))
