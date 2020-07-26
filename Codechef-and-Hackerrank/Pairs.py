"""
Question link:
https://www.hackerrank.com/challenges/pairs/problem
"""

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, nums):
    i=0
    j=1
    count=0
    n=len(nums)
    nums.sort()
    while(j < n):
        diff = nums[j] - nums[i];
        if (diff == k):
            count+=1
            j+=1
        elif (diff > k):
            i+=1
        elif (diff < k):
            j+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
