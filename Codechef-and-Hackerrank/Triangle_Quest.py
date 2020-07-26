"""
Question link:
https://www.hackerrank.com/challenges/python-quest-1/problem

Print the sequence
1
22
333
4444...
using only a single for loop and print statement
"""

for i in range(1,input()):
    print(i*(10**(i)/9))
