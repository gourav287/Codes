"""
Question link:
https://www.hackerrank.com/challenges/larrys-array/problem
"""

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(arr):
    s=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                s+=1
    if s%2==0:
        return("YES")
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
