"""
Question link:
https://www.hackerrank.com/challenges/new-year-chaos/problem
"""

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    s=0
    for i in range(len(q)):
        if (q[i]-i>3):
            print("Too chaotic")
            return
        else:
            for j in range(max(0,q[i]-2),i):
                if q[j]>q[i]:
                    s+=1
    print(s)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
